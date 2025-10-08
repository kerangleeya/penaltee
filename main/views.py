import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from main.forms import ProductForm
from main.models import Product
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json


@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)


    context = {
        'app_name' : 'Penaltee',
        'name': request.user.username,
        'class': 'PBD KI',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item =Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@csrf_exempt
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({
                    "success": True,
                    "message": "Your account has been successfully created!"
                })
            
            # Otherwise, normal redirect for non-AJAX form
            messages.success(request, "Your account has been successfully created!")
            return redirect('main:login')
        
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                errors = form.errors.as_json()
                return JsonResponse({
                    "success": False,
                    "message": "Username or password is invalid.",
                    "errors": errors
                }, status=400)

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.success(request, "Logged out successfully.")
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description")) # strip HTML tags
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        data = json.loads(request.body)

        name = data.get('name', '').strip()
        description = data.get('description', '').strip()
        price = data.get('price')
        category = data.get('category', '').strip()
        thumbnail = data.get('thumbnail', '').strip()
        is_featured = data.get('is_featured', False)

        if not name or not description or not price or not category:
            return JsonResponse({
                'success': False,
                'error': 'Name, description, price, and category are required.'
            }, status=400)

        try:
            price = float(price)
            if price < 0:
                raise ValueError
        except ValueError:
            return JsonResponse({
                'success': False,
                'error': 'Price must be a positive number.'
            }, status=400)

        product.name = name
        product.description = description
        product.price = price
        product.category = category
        product.thumbnail = thumbnail
        product.is_featured = is_featured
        product.save()

        return JsonResponse({
            'success': True,
            'message': 'Product updated successfully.',
            'product': {
                'id': str(product.id),
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'category': product.category,
                'thumbnail': product.thumbnail,
                'is_featured': product.is_featured,
                'user_id': product.user_id,
            }
        })

    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Product not found.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON data.'}, status=400)

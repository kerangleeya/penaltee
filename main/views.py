from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Penaltee',
        'name': 'Shelia Vellicita',
        'class': 'PBD KI'
    }

    return render(request, "main.html", context)
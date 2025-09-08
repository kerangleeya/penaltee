from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'penaltee',
        'name': 'Shelia Vellicita',
        'class': 'PBD KI'
    }

    return render(request, "main.html", context)
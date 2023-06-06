from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def blog(request):
    content = {
        'maqola': Maqola.objects.all()
    }
    return render(request, 'maqola.html', content)

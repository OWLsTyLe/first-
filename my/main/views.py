from django.shortcuts import render
from .models import Category

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    ads = Category.objects.all()
    return render(request, 'main/contact.html', {'ads': ads})



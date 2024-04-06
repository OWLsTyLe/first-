from django.shortcuts import render
from .models import Category

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
def js(request):
    return render(request, 'main/js.html')
def news(request):
    return render(request, 'main/news.html')
def stat(request):
    ads = Category.objects.all()
    return render(request, 'main/stat.html', {'ads': ads})
def cssvla(request):
    return render(request, 'main/csscel.html')
def teg(request):
    return render(request, 'main/teg.html')
def pod(request):
    return render(request, 'main/pod.html')
def globall(request):
    return render(request, 'main/global.html')


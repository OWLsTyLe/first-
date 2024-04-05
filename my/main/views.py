from django.shortcuts import render
from .models import Category

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    ads = Category.objects.all()
    return render(request, 'main/contact.html', {'ads': ads})
def js(request):
    return render(request, 'main/js.html')
def news(request):
    return render(request, 'main/news.html')
def stat(request):
    return render(request, 'main/stat.html')
def cssvla(request):
    return render(request, 'main/csscel.html')
def cssc(request):
    return render(request, 'main/cssc.html')
def teg(request):
    return render(request, 'main/teg.html')
def pod(request):
    return render(request, 'main/pod.html')
def globall(request):
    return render(request, 'main/global.html')
def jst(request):
    return render(request, 'main/jst.html')

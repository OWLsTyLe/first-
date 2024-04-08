from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm

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
def create(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'NO'

    form = CategoryForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)



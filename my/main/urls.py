from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('js', views.js, name='js'),
    path('news', views.news, name='news'),
    path('stat', views.stat, name='stat'),
    path('cssv', views.cssvla, name='cssvlast'),
    path('teg', views.teg, name='teg'),
    path('pod', views.pod, name='pod'),
    path('globall', views.globall, name='global'),
]

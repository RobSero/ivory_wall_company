from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('products/', views.productspage, name='products'),
    path('gallery/', views.gallerypage, name='gallery'),
    path('message/', views.messageSend, name='message')
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/', views.aboutpage),
    path('contact/', views.contactpage),
    path('portfolio/', views.portfoliopage),
]

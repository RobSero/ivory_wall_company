from django.shortcuts import render,redirect
from .forms import MessageForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.
def homepage(req):
  return render(req, 'pages/home.html')


def contactpage(req):
  if (req.POST):
    print('HE POSTED!')
    messages.success(req, 'Thank you for your message, we will get back to you as soon as possible')
  return render(req, 'pages/contact.html')


def productspage(req):
  return render(req, 'pages/products.html')


def gallerypage(req):
  return render(req, 'pages/gallery.html')

def messageSend(req):
  print(req.GET)
  query = MessageForm(req.GET)
  if query.is_valid():
    print('YEAH VALID')
    messages.info(req, 'WOOOOO DONE IT')
  else:
    messages.info(req, 'FAIL IN THE MAIL')
    print(messages.error)
  return render(req, 'pages/contact.html')
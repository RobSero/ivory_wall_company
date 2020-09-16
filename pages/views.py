from django.shortcuts import render
from .forms import MessageForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def homepage(req):
  return render(req, 'pages/home.html')


def aboutpage(req):
  return render(req, 'pages/about.html')


def productspage(req):
  return render(req, 'pages/products.html')


def gallerypage(req):
  
  context = {
    'items': [{
      'name' : 'green',
      'image_url' : 'https://res.cloudinary.com/dy7eycl8m/image/upload/v1591820610/brooklyn-nine-nine-fame-terry-crews-slammed-on-twitter-for-his-controversial-black-supremacy-tweet-001_jnwskm.jpg'
    },
           {
      'name' : 'red',
      'image_url' : 'https://res.cloudinary.com/dy7eycl8m/image/upload/v1591820610/brooklyn-nine-nine-fame-terry-crews-slammed-on-twitter-for-his-controversial-black-supremacy-tweet-001_jnwskm.jpg'
    },
           {
      'name' : 'blue',
      'image_url' : 'https://res.cloudinary.com/dy7eycl8m/image/upload/v1591820610/brooklyn-nine-nine-fame-terry-crews-slammed-on-twitter-for-his-controversial-black-supremacy-tweet-001_jnwskm.jpg'
    },
               {
      'name' : 'blue',
      'image_url' : 'https://res.cloudinary.com/dy7eycl8m/image/upload/v1591820610/brooklyn-nine-nine-fame-terry-crews-slammed-on-twitter-for-his-controversial-black-supremacy-tweet-001_jnwskm.jpg'
    },
                   {
      'name' : 'blue',
      'image_url' : 'https://res.cloudinary.com/dy7eycl8m/image/upload/v1591820610/brooklyn-nine-nine-fame-terry-crews-slammed-on-twitter-for-his-controversial-black-supremacy-tweet-001_jnwskm.jpg'
    },
                       {
      'name' : 'blue',
      'image_url' : 'https://res.cloudinary.com/dy7eycl8m/image/upload/v1591820610/brooklyn-nine-nine-fame-terry-crews-slammed-on-twitter-for-his-controversial-black-supremacy-tweet-001_jnwskm.jpg'
    },
           ]
  }
  
  return render(req, 'pages/gallery.html',{'context' : context})

def messageSend(req):
  print(req.POST)
  message = MessageForm(req.POST)
  if message.is_valid():
    print('YEAH VALID')
    messages.success(req, 'WOOOOO DONE IT')
  messages.error(req, 'FAIL IN THE MAIL')
  print(message.errors)
  return JsonResponse({'success':'yoyoyo'})
from django.shortcuts import render

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
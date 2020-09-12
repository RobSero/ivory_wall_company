from django.shortcuts import render

# Create your views here.
def homepage(req):
  return render(req, 'pages/home.html')


def aboutpage(req):
  return render(req, 'pages/about.html')


def contactpage(req):
  return render(req, 'pages/contact.html')


def portfoliopage(req):
  return render(req, 'pages/portfolio.html')
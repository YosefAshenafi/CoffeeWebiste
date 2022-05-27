from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'website/home.html', {})

def about_us(request):
    return render(request, 'website/about-us.html', {})

def gallery(request):
    return render(request, 'website/gallery.html', {})

def contact(request):
    return render(request, 'website/contact.html', {})

def products(request):
    return render(request, 'website/products.html', {})

def product_details(request):
    return render(request, 'website/product_details.html', {})

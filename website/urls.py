from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us.html', views.about_us, name='about'),
    path('gallery.html', views.gallery, name='gallery'),
    path('contact.html', views.contact, name='contact'),
    path('products.html', views.products, name='products'),
    path('product_details.html', views.product_details, name='product_details'),
]

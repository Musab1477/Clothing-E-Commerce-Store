"""
URL configuration for ecomWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('shop/category/<int:category_id>', views.shop, name='products_by_category'),
    path('shop/size/<int:size_id>', views.shop, name='products_by_size'),
    path('shop/search', views.shop, name='products_by_search'),
    path('about', views.about, name='about'),
    path('blogDetails', views.blogDetails, name='blogDetails'),
    path('blog', views.blog, name='blog'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main'),
    path('shopDetails/<int:productId>/', views.shopDetails, name='shopDetails'),
    path('shoppingCart', views.shoppingCart, name='shoppingCart'),
    path('wishlist', views.wishlist, name='wishlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

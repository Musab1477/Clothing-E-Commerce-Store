from django.shortcuts import render, get_object_or_404
from . models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def shop(request, category_id=None, size_id=None):
    
    search = request.GET.get('Search')
    
    categories = category.objects.all()
    sizes = size.objects.all()
    
    selected_category = None
    selected_size = None
    if category_id:
        selected_category = get_object_or_404(category, pk=category_id)
        products = product.objects.filter(productCategory=selected_category)
    
    elif size_id:
        selected_size = get_object_or_404(size, pk=size_id)
        products = product.objects.filter(productSize=selected_size)
        
    elif search:
        products = product.objects.all()
        products = products.filter(productName__icontains=search)
        
    else:
        selected_category = None
        products = product.objects.all()
        
    return render(request,'shop.html',{'products':products, 'sizes': sizes, 'categories': categories, 'selected_category': selected_category, 'selected_size': selected_size})

def about(request):
    return render(request, 'about.html')

def blogDetails(request):
    return render(request, 'blogDetails.html')

def blog(request):
    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def main(request):
    return render(request, 'main.html')

def shopDetails(request, productId):
    products = product.objects.get(productId=productId)
    allProducts = product.objects.all()  
    return render(request, 'shopDetails.html', {'products': products, 'allProducts': allProducts})

def shoppingCart(request):
    return render(request, 'shoppingCart.html')

def wishlist(request):
    return render(request, 'wishlist.html')

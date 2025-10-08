from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def homepage(request):
    featured_products = Product.objects.filter(is_active=True)[:6]  # Show first 6 products
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'product_detail.html', {'product': product})

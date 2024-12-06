
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product



def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    return redirect('kdeco:cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [
        {'product': product, 'quantity': cart[str(product.id)]}
        for product in products
    ]
    return render(request, 'kdeco/product/cart.html', {
        'cart_items': cart_items
    })

#def detail(request, product_id):
    #product = get_object_or_404(Product, id=product_id)
    #return render(request, 'kdeco/product/detail.html', {'product': product})

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'kdeco/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'kdeco/product/detail.html', {'product': product})

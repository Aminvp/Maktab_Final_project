from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import AddStoreForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.forms import CartAddForm


@login_required(login_url='accounts:user_login')
def add_store(request, id):
    if request.user.id == id:
        if request.method == 'POST':
            form = AddStoreForm(request.POST)
            if form.is_valid():
                new_store = form.save(commit=False)
                new_store.user = request.user
                new_store.save()
                messages.warning(request, 'Your store is under review. The result will be announced later!', 'warning')
                return redirect('accounts:panel')
        else:
            form = AddStoreForm()
            return render(request, 'shop/add_store.html', {'form': form})
    else:
        return redirect('shop:home')


def home(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = CartAddForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})

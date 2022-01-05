from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Product, Category, Store
from .forms import AddStoreForm, AddProductForm, EditProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.forms import CartAddForm


def home(request, slug=None):
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    store = product.store
    form = CartAddForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'store': store, 'form': form})


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
                return redirect('accounts:panel', id)
        else:
            form = AddStoreForm()
            return render(request, 'shop/add_store.html', {'form': form})
    else:
        return redirect('shop:home')


# @login_required(login_url='accounts:user_login')
# def remove_store(request, id, store_id):
#     if request.user.id == id:



@login_required(login_url='accounts:user_login')
def add_product(request, id, store_id):
    if request.user.id == id:
        store = get_object_or_404(Store, id=store_id)
        if request.method == 'POST' and store.status == 'confirmed':
            form = AddProductForm(request.POST, request.FILES)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.store = store
                new_product.save()
                messages.success(request, 'Your product has been successfully added', 'success')
                form.save_m2m()
                return redirect('accounts:panel', id)
        else:
            form = AddProductForm()
            messages.warning(request, 'Your store status is being reviewed!', 'warning')
            return render(request, 'shop/add_product.html', {'form': form})
    else:
        return redirect('shop:home')


@login_required(login_url='accounts:user_login')
def edit_product(request, id, store_id, product_id):
    if request.user.id == id:
        store = get_object_or_404(Store, id=store_id)
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            form = EditProductForm(request.POST, instance=product)
            if form.is_valid():
                ep = form.save(commit=False)
                store.status = 'pending'
                store.save()
                ep.save()
                print(store.status)
                messages.success(request, 'Your product edited successfully', 'success')
                return redirect('accounts:panel', id)
        else:
            form = EditProductForm(instance=product)
            return render(request, 'shop/edit_product.html', {'form': form})
    else:
        return redirect('shop:home')
















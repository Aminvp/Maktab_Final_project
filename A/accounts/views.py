from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, PhoneLoginForm, VerifyCodeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Profile
from blog.models import Post
from django.contrib.auth.decorators import login_required
from shop.models import Product, Store
from random import randint
from kavenegar import *
from django import forms


def user_login(request):
    next = request.GET.get('next')
    print(next)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                if next:
                    print(next)
                    return redirect(next)
                return redirect('shop:home')
        else:
            messages.error(request, 'email or password is wrong', 'danger')
            return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password1'])
            user.save()
            login(request, user)
            messages.success(request, 'you registered successfully', 'success')
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required(login_url='accounts:user_login')
def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('shop:home')


@login_required(login_url='accounts:user_login')
def user_dashboard(request, id):
    user = get_object_or_404(User, id=id)
    posts = Post.objects.filter(user=user)
    self_dash = False
    if request.user.id == id:
        self_dash = True
    return render(request, 'accounts/dashboard.html', {'user': user, 'posts': posts, 'self_dash': self_dash})


def user_panel(request, id):
    user = get_object_or_404(User, id=id)
    store = Store.objects.get(user=user)
    products = Product.objects.filter(store=store)
    return render(request, 'accounts/panel.html', {'user': user, 'store': store, 'products': products})


def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            global phone, rand_num
            phone = f"0{form.cleaned_data['phone']}"
            rand_num = randint(1000, 9999)
            api = KavenegarAPI('467066542F7547496B7A2F34516745504D7173656E4934762F6F6243726B565A476F556B764D597A6F736F3D')
            params = {'sender': '', 'receptor': phone, 'message': rand_num}
            response = api.sms_send( params)
            return redirect('accounts:verify')
    else:
        form = PhoneLoginForm()
    return render(request, 'accounts/phone_login.html', {'form': form})


def verify(request):
    if request.method == 'POST':
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            if rand_num == form.cleaned_data['code']:
                profile = get_object_or_404(Profile, phone=phone)
                user = get_object_or_404(User, Profile__id=profile.id)
                login(request, user)
                messages.success(request, 'logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'your code is wrong', 'warning')
    else:
        form = VerifyCodeForm()
    return render(request, 'accounts/verify.html', {'form': form})


















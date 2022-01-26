from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, PhoneLoginForm, VerifyCodeForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Profile
from blog.models import Post
from django.contrib.auth.decorators import login_required
from shop.models import Product, Store
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from random import randint
from kavenegar import *
import re


class UserLogin(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'your logged in successfully', 'info')
                return redirect('shop:home')
            messages.error(request, 'email or password is wrong!', 'warning')
        return render(request, self.template_name, {'form': form})


class UserRegister(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password1'])
            # login(request, user)
            messages.success(request, 'your registered successfully', 'info')
            return redirect('shop:home')
        return render(request, self.template_name, {'form': form})


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'your logged out successfully', 'info')
        return redirect('shop:home')


class UserDashboard(LoginRequiredMixin, View):
    template_name = 'accounts/dashboard.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        posts = Post.objects.filter(user=user)
        if user.phone:
            if re.search('^(\+98|0098|98|0)?9\d{9}$', user.phone):
                result = re.finditer('9\d{9}$', user.phone)
                for number in result:
                    print('0' + number.group())
            else:
                messages.warning(request, 'Your phone number has not been verified, please review it in the profile editing section!', 'warning')
        self_dash = False
        if request.user.id == user_id:
            self_dash = True
        return render(request, self.template_name, {'user': user, 'posts': posts, 'self_dash': self_dash})


class ProfileEdit(LoginRequiredMixin, View):
    form_class = EditProfileForm
    template_name = 'accounts/edit_profile.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = self.form_class(instance=request.user.profile, initial={'email': request.user.email, 'full_name': request.user.full_name, 'phone': request.user.phone})
        return render(request, self.template_name, {'user': user, 'form': form})

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = self.form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            user.email = form.cleaned_data['email']
            user.full_name = form.cleaned_data['full_name']
            user.phone = form.cleaned_data['phone']
            user.save()
            messages.success(request, 'your profile edited successfully', 'info')
            return redirect('accounts:dashboard', user_id)


class UserPanel(LoginRequiredMixin, View):
    template_name = 'accounts/panel.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        store = Store.objects.get(user=user)
        products = Product.objects.filter(store=store)
        return render(request, self.template_name, {'user': user, 'store': store, 'products': products})


def phone_login(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            global phone, rand_num
            phone = f"0{form.cleaned_data['phone']}"
            rand_num = randint(1000, 9999)
            api = KavenegarAPI('467066542F7547496B7A2F34516745504D7173656E4934762F6F6243726B565A476F556B764D597A6F736F3D')
            params = {'sender': '', 'receptor': phone, 'message': rand_num}
            api.sms_send(params)
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


















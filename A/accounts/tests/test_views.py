from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, Profile
from accounts.forms import UserRegistrationForm


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('accounts:user_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.failUnless(response.context['form'], UserRegistrationForm)

    def test_user_register_POST_valid(self):
        response = self.client.post(reverse('accounts:user_register'), data={
            'email': 'hasan@gmail.com',
            'full_name': 'hasan yazdani',
            'password1': '12345',
            'password2': '12345'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)

    def test_user_register_POST_invalid(self):
        response = self.client.post(reverse('accounts:user_register'), data={
            'email': 'invalid_email',
            'full_name': 'meysam akbary',
            'password1': '12345',
            'password2': '12345'
        })
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field='email', errors=['Enter a valid email address.'])

    def test_user_dashboard_GET(self):
        User.objects.create_user(email='hamed@gmail.com', full_name='hamed yazdani', password='12345')
        self.client.login(email='hamed@gmail.com', password='12345')
        response = self.client.get(reverse('accounts:dashboard', args=[1, ]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')

















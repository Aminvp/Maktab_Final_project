from django.test import TestCase
from accounts.forms import UserRegistrationForm, UserLoginForm


class TestRegistrationForm(TestCase):
    def test_valid_data(self):
        form = UserRegistrationForm(data={'email': 'amin@gmail.com', 'full_name': 'amin verdipour', 'password1': 'root', 'password2': 'root'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserRegistrationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)


class TestLoginForm(TestCase):
    def test_valid_data(self):
        form = UserLoginForm(data={'email': 'amin@gmail.com', 'password': 'root'})
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
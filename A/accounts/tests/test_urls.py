from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import UserRegister, UserLogin, UserLogout, UserDashboard, UserPanel
from accounts.api_views import UserView, MyObtainTokenPairView, UserIdView, ProfileView, ProfileIdView


class TestUrls(SimpleTestCase):
    def test_register(self):
        url = reverse('accounts:user_register')
        self.assertEqual(resolve(url).func.view_class, UserRegister)

    def test_login(self):
        url = reverse('accounts:user_login')
        self.assertEqual(resolve(url).func.view_class, UserLogin)

    def test_logout(self):
        url = reverse('accounts:user_logout')
        self.assertEqual(resolve(url).func.view_class, UserLogout)

    def test_dashboard(self):
        url = reverse('accounts:dashboard', args=[3])
        self.assertEqual(resolve(url).func.view_class, UserDashboard)

    def test_panel(self):
        url = reverse('accounts:panel', args=[2])
        self.assertEqual(resolve(url).func.view_class, UserPanel)

    def test_api_user_register(self):
        url = reverse('accounts:api_user_register')
        self.assertEqual(resolve(url).func.view_class, UserView)

    def test_api_user_login(self):
        url = reverse('accounts:token_obtain_pair')
        self.assertEqual(resolve(url).func.view_class, MyObtainTokenPairView)

    def test_api_user_update(self):
        url = reverse('accounts:api_user_update', args=[5])
        self.assertEqual(resolve(url).func.view_class, UserIdView)

    def test_api_profile_create(self):
        url = reverse('accounts:api_profile_create')
        self.assertEqual(resolve(url).func.view_class, ProfileView)

    def test_api_profile_update(self):
        url = reverse('accounts:api_profile_update', args=[8])
        self.assertEqual(resolve(url).func.view_class, ProfileIdView)















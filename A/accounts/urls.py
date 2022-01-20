from django.urls import path, include
from . import views
from . import api_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'accounts'


api_urls = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/login/', api_views.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('users/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', api_views.UserView.as_view(), name='api_user_register'),
    path('users/<int:pk>/', api_views.UserIdView.as_view(), name='api_user_update'),
    path('users/profiles/', api_views.ProfileView.as_view(), name='api_profile_create'),
    path('users/profiles/<int:pk>/', api_views.ProfileIdView.as_view(), name='api_profile_update'),
]

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('logout/', views.UserLogout.as_view(), name='user_logout'),
    path('dashboard/<int:user_id>/', views.UserDashboard.as_view(), name='dashboard'),
    path('edit_profile/<int:user_id>/', views.ProfileEdit.as_view(), name='edit_profile'),
    path('panel/<int:user_id>/', views.UserPanel.as_view(), name='panel'),
    path('phone_login/', views.phone_login, name='phone_login'),
    path('verify/', views.verify, name='verify'),
    path('api/', include(api_urls)),
]



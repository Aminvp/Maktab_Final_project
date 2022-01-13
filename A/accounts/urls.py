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
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/<int:id>/', views.user_dashboard, name='dashboard'),
    path('panel/<int:id>/', views.user_panel, name='panel'),
    path('api/', include(api_urls)),
]



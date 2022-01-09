from django.urls import path, include
from . import views
from . import api_views


app_name = 'accounts'

api_urls = [
    path('users/', api_views.UserListView.as_view()),
    path('users/register/', api_views.UserRegisterView.as_view()),
    path('users/login/', api_views.UserLoginView.as_view()),
    path('users/detail/<int:pk>/', api_views.UserDetailView.as_view()),
    path('users/update/<int:pk>/', api_views.UserUpdateView.as_view()),
    path('users/delete/<int:pk>/', api_views.UserDeleteView.as_view()),
    path('users/profiles/', api_views.ProfileListView.as_view()),
    path('users/profiles/detail/<int:pk>/', api_views.ProfileDetailView.as_view()),
    path('users/profiles/create/', api_views.ProfileCreateView.as_view()),
    path('users/profiles/update/<int:pk>/', api_views.ProfileUpdateView.as_view()),
]

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/<int:id>/', views.user_dashboard, name='dashboard'),
    path('panel/<int:id>/', views.user_panel, name='panel'),
    path('api/', include(api_urls))
]
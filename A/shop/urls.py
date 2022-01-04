from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.home, name='category_filter'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_store/<int:id>/', views.add_store, name='add_store'),
    path('add_product/<int:id>/<int:store_id>/', views.add_product, name='add_product'),
    path('edit_product/<int:id>/<int:store_id>/<int:product_id>/', views.edit_product, name='edit_product'),
]
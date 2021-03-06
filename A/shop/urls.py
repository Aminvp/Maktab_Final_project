from django.urls import path, include
from . import views
from . import api_views

app_name = 'shop'


api_urls = [
    path('stores/', api_views.StoreListView.as_view()),
    path('stores/confirmed/', api_views.StoreConfirmedView.as_view()),
    path('stores/products/', api_views.ProductListView.as_view()),
    path('stores/<int:pk>/products/', api_views.ProductStoreView.as_view()),
]


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.home, name='category_filter'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_store/<int:id>/', views.add_store, name='add_store'),
    path('remove_store/<int:id>/<int:store_id>/', views.remove_store, name='remove_store'),
    path('add_product/<int:id>/<int:store_id>/', views.add_product, name='add_product'),
    path('edit_product/<int:id>/<int:store_id>/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/<int:product_id>/', views.delete_product, name='delete_product'),
    path('api/', include(api_urls)),
]
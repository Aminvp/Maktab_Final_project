from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('all_posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('add_post/<int:id>/', views.add_post, name='add_post'),
    path('post_delete/<int:id>/<int:post_id>/', views.post_delete, name='post_delete'),
    path('post_edit/<int:id>/<int:post_id>/', views.post_edit, name='post_edit'),
    path('all_category/', views.all_category, name='all_category'),
    path('all_category/<int:id>/', views.category_detail, name='category_detail'),
    path('add_reply/<int:post_id>/<int:comment_id>', views.add_reply, name='add_reply'),
    path('add_category/', views.add_category, name='add_category'),
    path('category_edit/<int:category_id>/', views.category_edit, name='category_edit'),
    path('category_delete/<int:category_id>/', views.category_delete, name='category_delete'),
]
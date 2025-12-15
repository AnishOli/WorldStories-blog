from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    #crud for category
    path('categories/', views.categories, name="categories"),
    path('categories/add/', views.add_category, name="add_category"),
    path('categories/edit/<int:pk>/', views.edit_category, name="edit_category"),
    path('categories/delete/<int:pk>/', views.delete_category, name="delete_category"),

    #curd for blog

    path('blog_posts/',views.blog_posts, name= 'blog_posts'),
    path('blog_posts/add/',views.add_posts, name= 'add_posts'),
    # path('edit',views.posts, name= 'posts'),
    # path('delete',views.posts, name= 'posts'),
    
]

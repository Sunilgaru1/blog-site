from django.urls import path
from . import views

urlpatterns = [
    
    
    path('home/',views.BlogView,name='blog_list'),
    path('',views.BlogView,name='blog_list'),
    path('create/',views.CreateBlog,name = 'create_blog'),

    path('blog/<int:pk>/',views.BlogDetails,name = 'blog_detail'),

    path('edit/<int:pk>/', views.EditBlog, name='edit_blog'),
    path('delete/<int:pk>/', views.DeleteBlog, name='delete_blog'),

    path('register/', views.RegisterView, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('login/', views.LoginView, name='login'),
]
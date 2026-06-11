from django.urls import path
from . import views

urlpatterns = [
    
    path('blogs/',views.BlogView,name='blog_list'),
    path('create/',views.CreateBlog,name = 'create_blog'),
]


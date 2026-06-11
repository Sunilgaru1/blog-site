from django.shortcuts import render
from .models import BlogModel
# Create your views here.

def BlogView(request):
    blogdata = BlogModel.objects.all()

    return render(request,'blog/blog_index.html',{'blogdata':blogdata})
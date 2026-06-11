from django.shortcuts import render , redirect
from .models import BlogModel
from .forms import BlogForm

# Create your views here.

def BlogView(request):
    blogdata = BlogModel.objects.all()

    return render(request,'blog/blog_index.html',{'blogdata':blogdata})

def CreateBlog(request):

    form = BlogForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('blog_list')
        return render(request,'blog/blog_create.html',{'form':form})
        
    else:
        form = BlogForm()
        return render(request,'blog/blog_create.html',{'form':form})
    
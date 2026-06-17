from django.shortcuts import render , redirect
from .models import BlogModel
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def BlogView(request):
    blogdata = BlogModel.objects.order_by('-created')

    return render(request,'blog/blog_index.html',{'blogdata':blogdata})

@login_required
def CreateBlog(request):

    form = BlogForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            return redirect('blog_list')
        return render(request,'blog/blog_create.html',{'form':form})
        
    else:
        form = BlogForm()
        return render(request,'blog/blog_create.html',{'form':form})
    
from django.shortcuts import render, get_object_or_404

def BlogDetails(request, pk):
    blog = get_object_or_404(BlogModel, id=pk)

    return render(request, 'blog/blog_detail.html', {'blog': blog})


@login_required
def EditBlog(request, pk):

    blog = get_object_or_404(BlogModel, pk=pk)

    if (
        request.user != blog.owner
        and not request.user.is_staff
        and not request.user.is_superuser
    ):
        return HttpResponse("Permission Denied")

    if request.method == 'POST':

        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.id)

    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/blog_edit.html', {'form': form})


@login_required
def DeleteBlog(request, pk):

    blog = get_object_or_404(BlogModel, pk=pk)

    if (
        request.user != blog.owner
        and not request.user.is_staff
        and not request.user.is_superuser
    ):
        return HttpResponse("Permission Denied")

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')

    return render(request, 'blog/blog_delete.html', {'blog': blog})
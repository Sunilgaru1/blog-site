from django.shortcuts import render , redirect
from .models import BlogModel
from .forms import BlogForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def BlogView(request):

    query = request.GET.get('q')

    if query:
        blogdata = BlogModel.objects.filter(
            title__icontains=query
        ).order_by('-created')
    else:
        blogdata = BlogModel.objects.all().order_by('-created')

    return render(
        request,
        'blog/blog_index.html',
        {
            'blogdata': blogdata,
            'query': query
        }
    )

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

def RegisterView(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'blog/register.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('blog_list')

def LoginView(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('blog_list')

    else:
        form = AuthenticationForm()

    return render(request, 'blog/login.html', {'form': form})
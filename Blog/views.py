from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from Blog.models import Post
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm
import datetime, random
from django.db.models import Q, Sum

def showBlog(request):
    post = Post.objects.order_by('-id')[0:5]
    k = len(post)
    post1 = Post.objects.order_by('-id')[0:1]
    post2 = Post.objects.all().order_by('?')[:6]
    diction = {
        'post1':post1,
        'post':post,
        'post2':post2
    }
    return render(request, 'Blog/blog.html', context=diction)
def showBlog2(request, pk):
    post1 = Post.objects.filter(Q(id=str(pk)))
    post = Post.objects.order_by('-id')[0:5]
    post2 = Post.objects.all().order_by('?')[:6]
    diction = {
        'post1':post1,
        'post':post,
        'post2':post2
    }
    return render(request, 'Blog/blog.html', context=diction)
@login_required
def edit_blog(request, pk):
    blog = Post.objects.get(pk=pk)
    form = PostForm(instance=blog)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/post/list/')
    return render(request, 'Blog/create_blog.html', context={'form': form})
def delete_blog(request, pk):
    blog = Post.objects.get(pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('/post/list/')
    return render(request, 'Blog/delete_blog.html')
@login_required
def showBlogList(request):
    post = Post.objects.order_by('-id').all()
    return render(request, 'Blog/blog_list.html', context={'post':post})
@login_required
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_obj = form.save(commit=False)
            blog_obj.author = request.user
            title = blog_obj.title
            blog_obj.save()
            return redirect('/post/list/')
    return render(request, 'Blog/create_blog.html', context={'form':form})


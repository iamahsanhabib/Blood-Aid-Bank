from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'Blog'

urlpatterns = [
    path('post/list/', views.showBlogList, name = 'show_blog_list'),
    path('post/create/', views.create_post, name = 'create_post'),
    path('post/edit/<str:pk>/', views.edit_blog, name = 'edit_blog'),
    path('post/delete/<str:pk>/', views.delete_blog, name = 'delete_blog'),
    path('post/', views.showBlog, name = 'blog'),
    path('post/<int:pk>', views.showBlog2, name = 'blog1'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
    path('create_blog_post/', create_blog_post, name='create_blog_post'),
    path('my_blog_posts/', my_blog_posts, name='my_blog_posts'),
    path('blog_list/', blog_list, name='blog_list'),
    path('blog/<int:pk>/', blog_detail, name='blog_detail'),
]

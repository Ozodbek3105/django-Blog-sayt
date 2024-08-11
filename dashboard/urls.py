
from django.urls import path
from .views import *

urlpatterns = [
    
    path('',dashboard,name='dashboard'),
    path('categories/',categories,name='categories'),
    path('categories/add/',add_category,name='add_category'),
    path('categories/edit/<int:pk>/',edit_category,name='edit_category'),
    path('categories/delete/<int:id>/',delete_category,name='delete_category'),
    path('blogs/',blogs,name='blogs'),
    path('blogs/add/',add_blogs,name='add_blogs'),
    path('blogs/edit/<int:pk>/',edit_blogs,name='edit_blogs'),
    path('blogs/delete/<int:id>/',delete_blog,name='delete_blog'),
    path('users/',users,name='users'),
    path('users/add/',add_user,name='add_user'),
    path('users/edit/<int:pk>/',edit_user,name='edit_user'),
    path('users/delete/<int:id>/',delete_user,name='delete_user'),
]

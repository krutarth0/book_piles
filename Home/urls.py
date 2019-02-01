from django.contrib import admin
from django.urls import path
from .views import (
	PostListView ,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView
)
from . import views 


urlpatterns = [
    path('',views.PostListView.as_view(),name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<slug:slug>/',views.PostDetailView.as_view(),name='post-detail'),
    path('new_post/',views.PostCreateView.as_view(),name='post-create'),
    path('post/<slug:slug>/update',views.PostUpdateView.as_view(),name='post-update'),
    path('post/<slug:slug>/delete',views.PostDeleteView.as_view(),name='post-delete'),		      
]
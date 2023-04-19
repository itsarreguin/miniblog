from typing import List

from django.urls import path

from posts.views import PostCreateView
from posts.views import PostDetailView
from posts.views import PostDeleteView


app_name: str = 'posts'

urlpatterns: List[path] = [
    path('new', PostCreateView.as_view(), name='create'),
    path('posts/<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('posts/<slug:slug>/delete', PostDeleteView.as_view(), name='delete')
]
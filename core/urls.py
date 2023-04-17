from typing import List

from django.urls import path
from django.contrib.auth.views import LogoutView

from core.views import IndexView
from core.views import LoginView
from core.views import SignUpView


app_name: str = 'core'

urlpatterns: List[path] = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', LogoutView.as_view(), name='logout')
]
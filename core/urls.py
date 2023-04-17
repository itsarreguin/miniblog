from typing import List

from django.urls import path

from core.views import IndexView


app_name: str = 'core'

urlpatterns: List[path] = [
    path('', IndexView.as_view())
]
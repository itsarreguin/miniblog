from typing import Any
from typing import Dict
from typing import Tuple

from django import forms
from django.utils.translation import gettext_lazy as _

from posts.models import Post


class PostCreateForm(forms.Form):
    
    title = forms.CharField(
        max_length=255, min_length=10, label=_('Title'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-lg rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full py-2 px-4',
                'placeholder': 'My fancy title'
            }
        )
    )
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full py-4 px-4',
                'placeholder': 'Write a short description',
                'rows': '3'
            }
        )
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full py-4 px-4',
                'placeholder': 'Write your content here',
                'rows': '50'
            }
        )
    )
    
    def __init__(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        self.user = kwargs.pop('user', None)
        super(PostCreateForm, self).__init__(*args, **kwargs)
    
    def save(self, commit: bool = ...) -> Post:
        cleaned_data = self.cleaned_data
        Post.objects.create(
            author=self.user,
            **cleaned_data
        )
        return cleaned_data
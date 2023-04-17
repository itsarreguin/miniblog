from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    
    username = forms.CharField(
        max_length=30, min_length=4, label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        max_length=256, min_length=8, label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'Password'
            }
        )
    )


class SignUpForm(forms.Form):
    
    first_name = forms.CharField(
        max_length=50, min_length=2, label=_('First name'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'Guido'
            }
        )
    )
    last_name = forms.CharField(
        max_length=50, min_length=2, label=_('Last name'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'Van Rossum'
            }
        )
    )
    username = forms.CharField(
        max_length=50, min_length=2, label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'guidovanrossum'
            }
        )
    )
    email = forms.EmailField(
        max_length=200, min_length=10, label=_('Email address'),
        widget=forms.EmailInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': 'email@example.com'
            }
        )
    )
    password = forms.CharField(
        max_length=256, min_length=8, label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'bg-gray-700 border border-gray-500 text-white text-base rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5',
                'placeholder': '●●●●●●●●●●●●●'
            }
        )
    )
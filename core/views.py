from typing import Any
from typing import Dict
from typing import Type

from django.http import HttpRequest
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import FormMixin
from django.views.generic import TemplateView
from django.forms import Form
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from core.models import User
from posts.models import Post
from core.forms import LoginForm
from core.forms import SignUpForm


class IndexView(TemplateView):
    
    template_name = 'core/index.html'


class LoginView(FormMixin, View):
    
    form_class: Type[Form | ModelForm] = LoginForm
    template_name: str = 'core/login.html'
    template_title: str = _('Login')
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.template_title
        context['form'] = self.form_class
        
        return context
    
    def get(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('core:index')
        
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    
    def post(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            login(request, user=user)
            
            return redirect('core:index')
        
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class SignUpView(FormMixin, View):
    
    form_class: Type[Form | ModelForm] = SignUpForm
    template_name: str = 'core/signup.html'
    template_title: str = _('Sign Up')
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.template_title
        context['form'] = self.form_class
        
        return context
    
    def get(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect('core:index')
        
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    
    def post(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = User.objects.create_user(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user=user)

            return redirect('core:index')
        
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
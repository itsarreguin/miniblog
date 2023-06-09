from typing import Any
from typing import Dict
from typing import Type

from django.http import HttpRequest
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Model
from django.forms import Form
from django.forms import ModelForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from posts.models import Post
from posts.models import Comment
from posts.forms import PostCreateForm


class PostCreateView(LoginRequiredMixin, FormMixin, View):
    
    form_class: Type[Form | ModelForm]  = PostCreateForm
    template_name: str = 'posts/create.html'
    template_title: str = _('New post')
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.template_title
        context['form'] = self.get_form_class()
        
        return context
    
    def get(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    
    def post(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        form = self.form_class(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('core:index')
        
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)


class PostDetailView(DetailView):
    
    model: Type[Model] = Post
    template_name: str = 'posts/detail.html'
    slug_field: str = 'slug'
    slug_url_kwarg: str = 'slug'
    
    def get_context_data(self, **kwargs: Dict[str, Any]) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.filter(slug=self.kwargs['slug']).first()
        context['comments'] = Comment.objects.filter(post__slug=self.kwargs['slug']).all()
        
        return context


class PostDeleteView(LoginRequiredMixin, FormMixin, View):
    
    model: Type[Model] = Post
    template_name: str = 'posts/confirm.html'
    template_title: str = 'Delete post'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.template_title
        
        return context
    
    def post(self, request: HttpRequest, **kwargs: Dict[str, Any]) -> HttpResponse:
        article = self.model.objects.filter(slug=kwargs['slug']).first()
        if article:
            article.delete()
            return redirect('core:index')
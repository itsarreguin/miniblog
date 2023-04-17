from typing import Any
from typing import Dict
from typing import Tuple

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Post(models.Model):
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=200, unique=True, blank=False, null=False)
    body = models.TextField(_('body'), blank=False, null=False)
    description = models.CharField(_('description'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    
    class Meta:
        verbose_name: str = _('Post')
        verbose_name_plural: str = _('Posts')
    
    def __str__(self) -> str:
        return '%s' % self.title
    
    def save(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        if self.slug is None:
            self.slug = slugify(self.title)
        
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    
    author = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField(_('content'), blank=False, null=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    
    class Meta:
        verbose_name: str = _('Comment')
        verbose_name_plural: str = _('Comments')
    
    def __str__(self) -> str:
        return 'Comment by %s' % self.author.username


class Like(models.Model):
    
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE,
        related_name='likes'
    )
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE,
        related_name='likes'
    )
    created = models.DateTimeField(_('created'), auto_now_add=True)
    
    class Meta:
        verbose_name: str = _('Like')
        verbose_name_plural: str = _('Likes')
    
    def __str__(self) -> str:
        return 'Like by %s' % self.user.username
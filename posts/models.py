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
    body = models.TextField(_('body'))
    description = models.CharField(_('description'), max_length=255, blank=False, null=False)
    slug = models.SlugField(_('slug'), max_length=200, unique=True)
    
    def __str__(self) -> str:
        return '%s' % self.title
    
    def save(self, *args: Tuple[Any], **kwargs: Dict[str, Any]) -> None:
        if self.slug is None:
            self.slug = slugify(self.title)
        
        return super(Post, self).save(*args, **kwargs)
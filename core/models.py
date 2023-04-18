from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    class Meta:
        verbose_name: str = _('User')
        verbose_name_plural: str = _('Users')
    
    @property
    def total_posts(self) -> int:
        return self.posts.count()
    
    @property
    def total_comments(self) -> int:
        return self.comments.count()
    
    @property
    def total_likes(self) -> int:
        return self.likes.count()
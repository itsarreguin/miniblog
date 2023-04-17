from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    
    class Meta:
        verbose_name: str = _('User')
        verbose_name_plural: str = _('Users')
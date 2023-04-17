from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'core'
    verbose_name: str = _('Core')
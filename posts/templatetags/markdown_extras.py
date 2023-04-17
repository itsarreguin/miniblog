import markdown as md

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter('markdown')
@stringfilter
def markdown(value) -> str:
    return md.markdown(
        text=value,
        extension_configs=['markdown.extensions.fenced_code']
    )
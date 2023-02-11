from django import template
from events.models import *

register = template.Library()

@register.simple_tag(name='get')
def get_categories(filter=None):
    pass
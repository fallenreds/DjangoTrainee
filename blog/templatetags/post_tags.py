from django import template
from ..models import Category

register = template.Library()

def get_categories(context, order, count):
    categories = Category.objects.filter(published=True).order_by(order)
    if count is not None:
        categories = categories[:count]
    return categories

@register.simple_tag(takes_context=True)
def total_categories(context, count=None, order='-name'):
    return get_categories(context, order, count)

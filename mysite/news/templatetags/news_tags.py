from django import template
from django.db.models import *

from news.models import Category

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    # categories = Category.objects.all()
    return {"categories": categories, "arg1": arg1, "arg2": arg2}

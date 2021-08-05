from django import template
from blogs.models import CategoryModel

register = template.Library()

@register.simple_tag
def get_categories_list():
    categories_list = CategoryModel.objects.all()
    return categories_list
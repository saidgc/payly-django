from django import template

register = template.Library()


@register.filter(name='split_breadcrumb')
def split_breadcrumb(value: str, arg: str):

    return value.split(arg)

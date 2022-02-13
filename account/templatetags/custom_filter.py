from datetime import datetime

from django import template

register = template.Library()


@register.filter
def parse_date(value: datetime, args=None):
    if args:
        return value.strftime(args)
    return value.strftime('%m/%d/%Y %-I:%M %p')


@register.filter
def add_str(arg1: str, arg2: str):
    return str(arg1) + str(arg2)

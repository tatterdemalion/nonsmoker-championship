from django import template
from django.utils.timezone import now

register = template.Library()


@register.filter(name='days')
def days(value):
    return (now() - value).days


@register.filter(name='score')
def score(value): 
    return '%.2f' % (int((now() - value).total_seconds()) / 100000.0)


@register.filter(name='battery')
def battery(value):
    days = (now() - value).days
    if days > 4:
        return 4
    return days

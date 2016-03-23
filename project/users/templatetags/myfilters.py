from django import template

register = template.Library()

@register.simple_tag
def addAttr(value, **kwargs):
    return value.as_widget(attrs=kwargs)
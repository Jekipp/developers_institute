from django import template

register = template.Library()

@register.filter(name='subtract')
def subtract(num1,num2):
    return num1 - num2
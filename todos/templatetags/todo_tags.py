from datetime import datetime
from django import template

register = template.Library()

@register.filter
def days_past(date):
    delta = datetime.now().date() - datetime.date(date) 
    return delta.days

@register.filter
def days_until(date):
    delta = date - datetime.now().date() 
    return delta.days
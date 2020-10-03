from django import template
from django.shortcuts import get_object_or_404

from booth import models
register = template.Library()

@register.simple_tag
def check_route_no(route_no):
    return route_no

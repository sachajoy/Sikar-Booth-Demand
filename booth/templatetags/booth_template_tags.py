from django import template
from django.shortcuts import get_object_or_404

from booth import models
register = template.Library()

@register.simple_tag('check_route')
def check_route_no(route_no):
    route = models.Route.objects.filter(route_no=route_no)
    if route.count() == 1:
        return route.xname
    else:
        return "Does Not Exists"

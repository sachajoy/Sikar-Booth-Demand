import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import (CreateView, ListView)

from booth import models
from booth.forms import booth


def check_route(request, route_id):
    print(route_id)
    # route = get_object_or_404(models.Route,route_no=route_id)
    route = models.Route.objects.filter(route_no=route_id).values('xname')
    if route.count() == 1:
        return HttpResponse(route[0]['xname'])
    return HttpResponse("No Route")



class BoothCreateListView(CreateView, ListView):
    context_object_name = 'booth_list'
    form_class = booth.BoothForm
    model = models.Booth
    template_name = 'booth/booth_create_list.html'


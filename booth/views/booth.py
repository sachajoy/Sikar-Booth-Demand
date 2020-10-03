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
    model = models.Booth
    form_class = booth.BoothForm
    template_name = 'booth/booth_create_list.html'
    context_object_name = 'booth_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        js_data = list(
            models.Route.objects.all().values_list('route_no', 'xname'))
        context['js_data'] = json.dumps(list(js_data), cls=DjangoJSONEncoder)
        return context

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView)

from booth import models
from booth.forms import route_form

class RouteCreateListView(CreateView):
    form = route_form.RouteCreateForm
    model = models.Route
    template_name = 'booth/route_create.html'

    def get_context_data(self, **kwargs):
        context = super(RouteCreateListView, self).get_context_data(**kwargs)
        context['route'] = models.Route.objects.all()
        return context


from django.views.generic import (CreateView, UpdateView, ListView)
import json
from django.core.serializers.json import DjangoJSONEncoder

from booth import models
from booth.forms import booth

class BoothCreateListView(CreateView, ListView):
    model = models.Booth
    form_class = booth.BoothForm
    template_name = 'booth/booth_create_list.html'
    context_object_name = 'booth_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        js_data = list(models.Route.objects.all().values_list('route_no', 'xname'))
        context['js_data'] = json.dumps(list(js_data), cls=DjangoJSONEncoder)
        return context

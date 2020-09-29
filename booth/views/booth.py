from django.views.generic import (CreateView, UpdateView, ListView)

from booth import models
from booth.forms import booth

class BoothCreateListView(CreateView, ListView):
    model = models.Booth
    form_class = booth.BoothForm
    template_name = 'booth/booth_create_list.html'
    context_object_name = 'booth_list'
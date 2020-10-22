from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (CreateView)

from booth import models
from booth.forms import booth


def check_route(request, route_id):
    print(route_id)
    # route = get_object_or_404(models.Route,route_no=route_id)
    route = models.Route.objects.filter(route_no=route_id).values('xname')
    if route.count() == 1:
        return HttpResponse(route[0]['xname'])
    return HttpResponse("No Route")


class BoothCreateListView(CreateView):
    # context_object_name = 'booth_list'
    form_class = booth.BoothForm
    model = models.Booth
    template_name = 'booth/booth_create_list.html'
    # success_url = 'booth:create-list-booth'

    def get_success_url(self):
        return reverse_lazy('booth:create-list-booth')

    def form_valid(self, form):
        booth = form.save(commit=False)
        booth.contractor_id = models.Route.objects.get(route_no=booth.route_no.route_no).contractor_id
        booth.tran_next_id = booth.booth_no * (10**7) + 1
        booth.uid = booth.booth_no
        booth.upwd = booth.booth_no
        booth.save()
        return super().form_valid(form=booth)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['booth_list'] = models.Booth.objects.all()
        # context['booth'] = models.boo
        return context

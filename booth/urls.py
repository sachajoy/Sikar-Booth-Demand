from django.urls import path

from booth.views import booth, route_view
from .views.index import index

app_name = 'booth'
urlpatterns = [
    path('', index, name='index'),
    path('create-list-booth/',
         booth.BoothCreateListView.as_view(),
         name='create-list-booth'),
    path('check-route/<int:route_id>',
         booth.check_route,
         name='check-route'),
    path('create-route/',
         route_view.RouteCreateListView.as_view(),
         name='create-route'),
]

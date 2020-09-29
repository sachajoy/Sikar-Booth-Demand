from django.urls import path

from booth.views import booth
from .views.index import index

app_name = 'booth'
urlpatterns = [
    path('', index, name='index'),
    path('create-list-booth/',
         booth.BoothCreateListView.as_view(),
         name='create-list-booth')
]

from django.urls import path
from .views.index import index

app_name = 'booth'
urlpatterns = [
    path('', index, name='index'),
]
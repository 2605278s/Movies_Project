from django.urls import path
from django.urls.resolvers import URLPattern
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.plotsPage), #name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path(route, view, opt olarak da name verilir)
]
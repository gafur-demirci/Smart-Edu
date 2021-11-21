from django.urls import path
from pages.views import IndexView, AboutView, ContactView
# from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    # path('about/', views.about, name="about"),
    # path('contact/', views.contact, name="contact"),
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    #path(route, view, opt olarak da name verilir)
]
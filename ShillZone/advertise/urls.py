from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdvertiseView.as_view(), name='advertise_view_link')
]
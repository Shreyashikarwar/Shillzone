from django.urls import path

from . import views

urlpatterns = [
    path('', views.OurPolicyView.as_view(), name='policy_view_link')
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_view_link'),
    path('search_page', views.SearchView.as_view(), name='search_view_link')
]
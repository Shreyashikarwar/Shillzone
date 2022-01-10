from django.shortcuts import render
from django.views import generic


class HomeView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home/index.html')

class SearchView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home/searchpage.html')

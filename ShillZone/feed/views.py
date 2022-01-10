from django.shortcuts import render
from django.views import generic

# Create your views here.

class FeedView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'feed/feed.html')

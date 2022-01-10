from django.shortcuts import render
from django.views import generic


class OurPolicyView(generic.View):

    def get(self, request, *args, **kwargs):
        return render(request, 'policy/ourpolicy.html')

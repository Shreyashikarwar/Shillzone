from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import AboutUs


class AboutView(generic.View):

    def get(self, request, *args, **kwargs):

        # about_data = get_object_or_404(AboutUs)
        about_data = AboutUs.objects.all()

        return render(request, 'about/about.html', {'about_data': about_data})


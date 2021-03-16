from django.views import View
from django.shortcuts import render
from properties.models import *


class IndexView(View):
    def get(self, request):
        context = {
            'home': 'true',
            'slider_properties': PropertyDescription.objects.order_by('-no_of_rooms')[:4],
            'latest_properties': PropertyDescription.objects.order_by('-no_of_rooms')[:4],
        }
        return render(request, 'properties/index.html', context)
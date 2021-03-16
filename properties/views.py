from django.shortcuts import render
from django.views import View
from .models import *


class Properties(View):
    def get(self, request):
        context = {
            'all_properties': 'true',
            'properties': PropertyDescription.objects.all(),
        }
        return render(request, 'properties/all_properties.html', context)

    def property_details(request):
        context = {
            'all_properties': 'true',
        }
        return render(request, 'properties/property-details.html', context)


class About(View):
    def get(self, request):
        context = {
            'about': 'true',
        }
        return render(request, 'properties/about.html', context)


class Contact(View):
    def get(self, request):
        context = {
            'contact': 'true',
        }
        return render(request, 'properties/contact.html', context)

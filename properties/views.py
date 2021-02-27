from django.shortcuts import render
from django.views import View


class Properties(View):
    def get(self, request):
        return render(request, 'properties/all_properties.html')

    def property_details(request):
        return render(request, 'properties/property-details.html')


class About(View):
    def get(self, request):
        return render(request, 'properties/about.html')


class Contact(View):
    def get(self, request):
        return render(request, 'properties/contact.html')

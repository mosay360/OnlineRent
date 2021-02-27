from django.urls import path
from .views import *

app_name = 'properties'
urlpatterns = (
    path('', Properties.as_view(), name="all_properties"),
    path('property_details', Properties.property_details, name="property_details"),
    path('about', About.as_view(), name="about"),
    path('contact', Contact.as_view(), name="contact"),
)
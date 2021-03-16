from django.contrib import admin
from .models import *


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ['owner', 'location', 'property_type', 'property_lease']


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Coordinates)
class CoordinatesAdmin(admin.ModelAdmin):
    pass


@admin.register(PropertyDescription)
class PropertyDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(ApiToken)
class ApiTokenAdmin(admin.ModelAdmin):
    pass

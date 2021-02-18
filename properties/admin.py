from django.contrib import admin
from .models import *


@admin.register(Properties)
class PropertiesAdmin(admin.ModelAdmin):
    pass


@admin.register(Corddinate)
class CorddinateAdmin(admin.ModelAdmin):
    pass


@admin.register(Property_Desc)
class PropertyDescAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment_Details)
class PaymentDetailsAdmin(admin.ModelAdmin):
    pass


@admin.register(ApiToken)
class ApiTokenAdmin(admin.ModelAdmin):
    pass

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Position(models.Model):
    title = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title

    """ Model for the property table """


class Properties(models.Model):
    PROPERTY_TYPE = [
        ('1', 'Apartment'),
        ('2', 'Land'),
        ('3', 'Full House'),
        ('4', 'Office Space'),
    ]
    LEASE_OPTIONS = [
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
        ('Lease', 'Lease'),
    ]
    property_title = models.CharField(max_length=60, blank=False)
    location = models.CharField(max_length=30)
    address = models.CharField(max_length=30, null=True)
    property_lease = models.CharField(max_length=100, choices=LEASE_OPTIONS)
    lease_options = models.CharField(max_length=50, blank=True)
    property_type = models.CharField(max_length=15, choices=PROPERTY_TYPE)
    duration = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    owner = models.CharField(max_length=30, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_title

    """ Model for property description """


class PropertyDescription(models.Model):
    images = models.ImageField(upload_to='properties/listings/', blank=True)
    has_balcony = models.BooleanField(default=False)
    price_negotiable = models.BooleanField(default=False)
    fully_furnished = models.BooleanField(default=False)
    no_of_rooms = models.IntegerField()
    no_of_baths = models.IntegerField()
    full_property_description = models.TextField()
    floor_area = models.IntegerField(blank=True)
    dimensions = models.CharField(max_length=30)
    reference = models.CharField(max_length=35, blank=True, null=True)
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference


""" Model for the cordinates """


class Coordinates(models.Model):
    cord1 = models.DecimalField
    cord2 = models.DecimalField
    cord3 = models.DecimalField
    cord4 = models.DecimalField
    prop_Id = models.ForeignKey(Properties, on_delete=models.CASCADE)

    """ Model for payment details """


class PaymentDetails(models.Model):
    user_email = models.EmailField(max_length=254)
    user_Id = models.CharField(max_length=50)
    ref_num = models.IntegerField
    isPaymentComplete = models.BooleanField
    prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_email


""" Model for the token """


class ApiToken(models.Model):
    text_secret_key = models.CharField(max_length=225)
    text_public_key = models.CharField(max_length=225)
    live_public_key = models.CharField(max_length=255)
    currency = models.DecimalField
    country_code = models.CharField(max_length=10)
    phone = models.IntegerField

    def __str__(self):
        return self.phone

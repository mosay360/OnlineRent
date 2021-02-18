from django.db import models

# Create your models here.

class Position(models.Model):
        title=models.CharField(max_length=100)

        """ Model for the property table """
class Properties(models.Model):
    location=models.CharField(max_length=100  , null=False)
    property_lease = models.CharField(max_length=100, null=False)
    property_type= models.CharField(max_length=100, null=False)
    duration = models.CharField(max_length=50, null=False)
    amount = models.DecimalField
    owner = models.CharField(max_length=100, null=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

""" Model for the cordinates """
class Corddinate(models.Model):
    cord1=models.DecimalField
    cord2= models.DecimalField
    cord3= models.DecimalField
    cord4=models.DecimalField
    prop_Id =models.ForeignKey(Properties, on_delete=models.CASCADE)

    """ Model for property description """
class Property_Desc(models.Model):
    images=models.CharField(max_length=255)
    no_rooms =models.IntegerField(10)
    no_bath= models.IntegerField(10)
    property_desc = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=100)
    prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)

    """ Model for payment details """
class Payment_Details(models.Model):
    user_email =models.EmailField( max_length=254)
    user_Id = models.CharField(max_length=50)
    ref_num = models.IntegerField
    isPaymentComplete= models.BooleanField
    prop_id= models.ForeignKey(Properties, on_delete=models.CASCADE)

""" Model for the token """
class ApiToken (models.Model):
    text_secret_key=models.CharField(max_length=225)
    text_public_key=models.CharField(max_length=225)
    live_public_key=models.CharField(max_length=255)
    currency = models.DecimalField
    country_code= models.CharField(max_length=10)
    phone = models.IntegerField





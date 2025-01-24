from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class User(models.Model):
    USER_TYPES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    usertype = models.CharField(max_length=10, choices=USER_TYPES)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.usertype})"
    
#Property  Model

class PropertyType(models.Model):
    property_type_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.property_type_name

class View(models.Model):
    view_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.view_name

class Features(models.Model):
    features_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.features_name

class Property(models.Model):
    PURCHASE_TYPES = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )

    type_of_purchase = models.CharField(max_length=10, choices=PURCHASE_TYPES)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    number_of_beds = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.FloatField()
    view = models.ForeignKey(View, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=50, unique=True)
    features = models.ForeignKey(Features, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.property_type} - {self.reference_number}"
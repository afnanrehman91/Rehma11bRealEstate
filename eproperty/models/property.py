from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

DEFAULT_USER_ID = 1


class Property(models.Model):
    propertyTitle = models.CharField(max_length=100)
    propertyCategory = models.ForeignKey('PropertyCategory', on_delete=models.CASCADE)
    propertySector = models.ForeignKey('PropertySector', on_delete=models.CASCADE)
    propertyFacing = models.ForeignKey('PropertyFacing', on_delete=models.CASCADE)
    propertyCountry = models.ForeignKey('Country', on_delete=models.CASCADE)
    propertyProvince = models.ForeignKey('Province', on_delete=models.CASCADE)
    propertyCity = models.ForeignKey('City', on_delete=models.CASCADE)
    propertyStreet = models.CharField(max_length=50)
    propertyPostalCode = models.CharField(max_length=6)
    propertyStreetNumber = models.CharField(max_length=5)
    propertyConstructionDate = models.DateField(default=datetime.date.today)
    propertyRegistrationDate = models.DateField(default=datetime.date.today)
    propertyNumberOfHalls = models.IntegerField(default=True)
    propertyNumberOfRooms = models.IntegerField(default=True)
    propertyNumberOfBathrooms = models.FloatField(default=True)
    propertyNumberOfFloors = models.IntegerField(default=True)
    propertyTotalArea = models.FloatField(default=True)
    propertyAskingPrice = models.FloatField(default=True)
    propertySellingPrice = models.FloatField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

    class Meta:
        verbose_name_plural = "Property"

    def __str__(self):
        return self.propertyTitle

    def get_absolute_url(self):
        return reverse('property-detail', kwargs={'pk': self.pk})


class PropertyCategory(models.Model):
    PROPERTY_CATEGORY = (
        ('Single House', 'Single House'),
        ('Attached House', 'Attached House'),
        ('Town House', 'Town House'),
        ('Apartment', 'Apartment'),
        ('Store', 'Store'),
        ('Farm', 'Farm'),
        ('Factory', 'Factory'),
        ('Mall', 'Mall'),
        ('Building', 'Building'),
        ('Other', 'Other')
    )
    propertyCategory = models.CharField(max_length=20, choices=PROPERTY_CATEGORY)

    class Meta:
        verbose_name_plural = "PropertyCategory"

    def __str__(self):
        return self.propertyCategory


class PropertySector(models.Model):
    PROPERTY_SECTOR = (
        ('Private', 'Private'),
        ('Residential', 'Residential'),
        ('Commercial', 'Commercial'),
        ('Government', 'Government'),
        ('Rural', 'Rural'),
        ('Other', 'Other')
    )
    propertySector = models.CharField(max_length=20, choices=PROPERTY_SECTOR)

    class Meta:
        verbose_name_plural = "PropertySector"

    def __str__(self):
        return self.propertySector


class PropertyFacing(models.Model):
    PROPERTY_FACING = (
        ('North', 'North'),
        ('South', 'South'),
        ('East', 'East'),
        ('West', 'West'),
        ('Other', 'Other')
    )
    propertyFacing = models.CharField(max_length=10, choices=PROPERTY_FACING)

    class Meta:
        verbose_name_plural = "PropertyFacing"

    def __str__(self):
        return self.propertyFacing


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    propertyImageDescription = models.CharField(max_length=100)
    propertyImage = models.ImageField(upload_to='uploadedImage/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "PropertyImage"

    def __str__(self):
        return self.propertyImageDescription


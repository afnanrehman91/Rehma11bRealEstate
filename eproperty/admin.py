from django.contrib import admin
from .models import Property, PropertyCategory, PropertySector, PropertyFacing, Province, Country, City, PropertyImage, Profile

admin.site.register(Property)
admin.site.register(PropertyCategory)
admin.site.register(PropertySector)
admin.site.register(PropertyFacing)
admin.site.register(PropertyImage)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Profile)

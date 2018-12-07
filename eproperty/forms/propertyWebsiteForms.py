from django import forms
from ..models import PropertyImage, Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['propertyTitle', 'propertyCategory', 'propertySector', 'propertyFacing', 'propertyCountry',
                  'propertyProvince', 'propertyCity', 'propertyStreet', 'propertyPostalCode', 'propertyStreetNumber',
                  'propertyConstructionDate', 'propertyRegistrationDate', 'propertyNumberOfHalls',
                  'propertyNumberOfRooms', 'propertyNumberOfBathrooms', 'propertyNumberOfFloors', 'propertyTotalArea',
                  'propertyAskingPrice', 'propertySellingPrice']


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['propertyImage', 'propertyImageDescription']

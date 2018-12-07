from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from eproperty.models import PropertyImage, Property
from eproperty.forms.propertyWebsiteForms import PropertyForm, PropertyImageForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)


# def home(request):
#     images = PropertyImage.objects.all().values('propertyImage', 'property__propertyTitle', 'property__propertyCategory'
#                                                 , 'property__propertySector', 'property__propertyFacing'
#                                                 , 'property__propertyCountry', 'property__propertyProvince'
#                                                 , 'property__propertyCity', 'property__propertyStreet'
#                                                 , 'property__propertyPostalCode', 'property__propertyStreetNumber'
#                                                 , 'property__propertyConstructionDate'
#                                                 , 'property__propertyRegistrationDate'
#                                                 , 'property__propertyNumberOfHalls', 'property__propertyNumberOfRooms'
#                                                 , 'property__propertyNumberOfBathrooms'
#                                                 , 'property__propertyNumberOfFloors'
#                                                 , 'property__propertyTotalArea', 'property__propertyAskingPrice'
#                                                 , 'property__propertySellingPrice'
#                                                 )
#
#     context = {
#         'images': images
#     }
#     return render(request, 'propertyWebsiteTemplates/home.html', context)


class AdvertListView(ListView):
    queryset = PropertyImage.objects.all().values('propertyImage', 'property__id', 'property__propertyTitle'
                                                , 'property__propertyCategory'
                                                , 'property__propertySector', 'property__propertyFacing'
                                                , 'property__propertyCountry', 'property__propertyProvince'
                                                , 'property__propertyCity', 'property__propertyStreet'
                                                , 'property__propertyPostalCode', 'property__propertyStreetNumber'
                                                , 'property__propertyConstructionDate'
                                                , 'property__propertyRegistrationDate'
                                                , 'property__propertyNumberOfHalls', 'property__propertyNumberOfRooms'
                                                , 'property__propertyNumberOfBathrooms'
                                                , 'property__propertyNumberOfFloors'
                                                , 'property__propertyTotalArea', 'property__propertyAskingPrice'
                                                , 'property__propertySellingPrice'
                                                  )
    print(queryset.all())
    template_name = 'propertyWebsiteTemplates/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'adverts'


class AdvertDetailView(DetailView):
    model = Property
    template_name = 'propertyWebsiteTemplates/propertyDetail.html'  # <app>/<model>_<viewtype>.html


class AdvertUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Property
    template_name = 'propertyWebsiteTemplates/updateAdvert.html'
    fields = ['propertyTitle', 'propertyCategory', 'propertySector', 'propertyFacing', 'propertyCountry',
              'propertyProvince', 'propertyCity', 'propertyStreet', 'propertyPostalCode', 'propertyStreetNumber',
              'propertyConstructionDate', 'propertyRegistrationDate', 'propertyNumberOfHalls',
              'propertyNumberOfRooms', 'propertyNumberOfBathrooms', 'propertyNumberOfFloors', 'propertyTotalArea',
              'propertyAskingPrice', 'propertySellingPrice']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.user:
            return True
        return False


class AdvertDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Property
    template_name = 'propertyWebsiteTemplates/delete.html'
    success_url = '/'

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.user:
            return True
        return False


def search(request):

    images = PropertyImage.objects.all().values('propertyImage', 'property__propertyTitle', 'property__propertyCategory'
                                                , 'property__propertySector', 'property__propertyFacing'
                                                , 'property__propertyCountry', 'property__propertyProvince'
                                                , 'property__propertyCity', 'property__propertyStreet'
                                                , 'property__propertyPostalCode', 'property__propertyStreetNumber'
                                                , 'property__propertyConstructionDate'
                                                , 'property__propertyRegistrationDate'
                                                , 'property__propertyNumberOfHalls', 'property__propertyNumberOfRooms'
                                                , 'property__propertyNumberOfBathrooms'
                                                , 'property__propertyNumberOfFloors'
                                                , 'property__propertyTotalArea', 'property__propertyAskingPrice'
                                                , 'property__propertySellingPrice'
                                                )

    query = request.GET.get("q")
    query1 = request.GET.get("q1")
    query2 = request.GET.get("q2")
    query3 = request.GET.get("q3")
    query4 = request.GET.get("q4")
    query5 = request.GET.get("q5")

    print("Base")
    print(images.all())

    if query:
        images = images.filter(
            Q(property__propertyTitle__icontains=query)
        )

    if query4:
        images = images.filter(
            Q(property__propertySellingPrice__gte=query4)
        )

    if query5:
        images = images.filter(
            Q(property__propertySellingPrice__lte=query5)
        )

    if query1:
        if query1 != '4':
            images = images.filter(
                Q(property__propertyNumberOfBathrooms=query1)
            )
        if query1 == '4':
            images = images.filter(
                Q(property__propertyNumberOfBathrooms__gte=query1)
            )
        print("Query 1")
        print(images.all())

    if query2:
        print(query2)
        if query2 != '4':
            print("property__propertyNumberOfRooms")
            images = images.filter(
                Q(property__propertyNumberOfRooms=query2)
            )
        if query2 == '4':
            print("property__propertyNumberOfRooms__gte")
            images = images.filter(
                Q(property__propertyNumberOfRooms__gte=query2)
            )
        print("Query 2")
        print(images.all())

    if query3:
        if query3 != '4':
            print("property__propertyNumberOfFloors")
            images = images.filter(
                Q(property__propertyNumberOfFloors=query3)
            )
        if query3 == '4':
            print("property__propertyNumberOfFloors__gte")
            images = images.filter(
                Q(property__propertyNumberOfFloors__gte=query3)
            )
        print("Query 3")
        print(images.all())

    context = {
        'images': images
    }
    return render(request, 'propertyWebsiteTemplates/search.html', context)


def contact(request):
    return render(request, 'propertyWebsiteTemplates/contact.html')


@login_required
@csrf_protect
def createAdvert(request):
    if request.method == "POST":
        propertyForm = PropertyForm(request.POST, request.FILES)
        propertyImageForm = PropertyImageForm(request.POST, request.FILES)

        if propertyForm.is_valid() and propertyImageForm.is_valid():
            propertyForm.instance.user = request.user
            property = propertyForm.save()
            image = propertyImageForm.save(False)
            image.property = property
            image.save()

        messages.success(request, f'Success: Advert Posted, scroll down to see all the adverts posted!!!')
        return redirect('property-home')

    else:
        propertyForm = PropertyForm()
        propertyImageForm = PropertyImageForm()

    args = {}
    args["propertyForm"] = propertyForm
    args["propertyImageForm"] = propertyImageForm
    return render(request, 'propertyWebsiteTemplates/createAdvert.html', args)


def about(request):
    return render(request, 'propertyWebsiteTemplates/about.html')

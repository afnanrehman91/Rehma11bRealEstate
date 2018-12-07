from django.urls import path
from eproperty.views import propertyWebsiteViews
from .views.propertyWebsiteViews import (
    AdvertListView,
    AdvertDetailView,
    AdvertUpdateView,
    AdvertDeleteView
)

urlpatterns = [
    path('', AdvertListView.as_view(), name='property-home'),
    path('advert/<int:pk>/', AdvertDetailView.as_view(), name='property-detail'),
    path('advert/<int:pk>/update/', AdvertUpdateView.as_view(), name='property-update'),
    path('advert/<int:pk>/delete/', AdvertDeleteView.as_view(), name='property-delete'),
    # path('', propertyWebsiteViews.home, name='property-home'),
    path('about/', propertyWebsiteViews.about, name='property-about'),
    path('contact/', propertyWebsiteViews.contact, name='property-contact'),
    path('createAdvert/', propertyWebsiteViews.createAdvert, name='property-create'),
    path('search/', propertyWebsiteViews.search, name='search-page'),
]

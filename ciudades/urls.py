from django.urls import path
from .city_api import CityListView, CityCreateView, CityRetriveView, CityUpdateView, CityDestroyView

urlpatterns = [
    path('cities/', CityListView.as_view(), name="cities"),
    path('cities/create', CityCreateView.as_view(), name="city_create"),
    path('cities/<int:id>/', CityRetriveView.as_view(), name="city"),
    path('cities/<int:id>/update/', CityUpdateView.as_view(), name="city_update"),
    path('cities/<int:id>/delete/', CityDestroyView.as_view(), name="city_delete")

]

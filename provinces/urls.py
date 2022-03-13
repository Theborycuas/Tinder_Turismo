from django.urls import path
from .province_api import ProvinceListView, ProvinceCreateView, ProvinceRetriveView, ProvinceUpdateView, ProvinceDestroyView

urlpatterns = [
    path('provinces/', ProvinceListView.as_view(), name="provinces"),
    path('provinces/create', ProvinceCreateView.as_view(), name="province_create"),
    path('provinces/<int:id>/', ProvinceRetriveView.as_view(), name="province"),
    path('provinces/<int:id>/update/', ProvinceUpdateView.as_view(), name="province_update"),
    path('provinces/<int:id>/delete/', ProvinceDestroyView.as_view(), name="province_delete")

]

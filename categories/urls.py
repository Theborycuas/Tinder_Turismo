from django.urls import path
from .category_api import CategoryListView, CategoryCreateView, CategoryRetriveView, CategoryUpdateView, CategoryDestroyView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('categories/create', CategoryCreateView.as_view(), name="category_create"),
    path('categories/<int:id>/', CategoryRetriveView.as_view(), name="category"),
    path('categories/<int:id>/update/', CategoryUpdateView.as_view(), name="category_update"),
    path('categories/<int:id>/delete/', CategoryDestroyView.as_view(), name="category_delete")

]

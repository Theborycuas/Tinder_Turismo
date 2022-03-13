from django.urls import path
from .tag_api import TagListView, TagCreateView, TagRetriveView, TagUpdateView, TagDestroyView

urlpatterns = [
    
    path('tags/', TagListView.as_view(), name="tags"),
    path('tags/create', TagCreateView.as_view(), name="tag_create"),
    path('tags/<int:id>/', TagRetriveView.as_view(), name="tag"),
    path('tags/<int:id>/update/', TagUpdateView.as_view(), name="tag_update"),
    path('tags/<int:id>/delete/', TagDestroyView.as_view(), name="tag_delete"),

]

from django.urls import path
from .user_api import UserListView, UserCreateView, UserRetriveView, UserUpdateView, UserDestroyView

urlpatterns = [
    path('users/', UserListView.as_view(), name="users"),
    path('users/create', UserCreateView.as_view(), name="user_create"),
    path('users/<int:id>/', UserRetriveView.as_view(), name="user"),
    path('users/<int:id>/update/', UserUpdateView.as_view(), name="user_update"),
    path('users/<int:id>/delete/', UserDestroyView.as_view(), name="user_delete")

]

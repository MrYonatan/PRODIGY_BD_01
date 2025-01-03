from django.urls import path
from .views import create_user, read_user, update_user, delete_user, listUsersView

urlpatterns = [
    path("users/", listUsersView, name="listUsers"),
    path("users/create/", create_user, name="create"),
    path("users/<str:user_id>/", read_user, name="read"),
    path("users/<str:user_id>/update/", update_user, name="update"),
    path("users/<str:user_id>/delete/", delete_user, name="delete"),
]

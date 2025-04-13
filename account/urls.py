from django.urls import path
from .views import UserListView, UserListCreateView


urlpatterns = [
    path("", UserListView.as_view()),
    path("create-user/", UserListCreateView.as_view()),
]

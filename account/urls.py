from django.urls import path
from .views import UserListView, UserListCreateView, user_profile
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView


urlpatterns = [
    path("", UserListView.as_view()),
    path("create-user/", UserListCreateView.as_view()),
    path("user-profile/", user_profile),
    path("login",TokenObtainPairView.as_view()),
    path("refresh", TokenRefreshView.as_view()),
    path("verify", TokenVerifyView.as_view())
]

from django.urls import path
from .views import UserListView, UserListCreateView, user_profile, CreateUserView, UpdateUserView, CreateUserView, DeleteUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView


urlpatterns = [
    path("", UserListView.as_view()),
    path("create-user/", UserListCreateView.as_view()),
    path("creare-user2/", CreateUserView.as_view()),
    path("user-profile/", user_profile),
    path("login",TokenObtainPairView.as_view()),
    path("refresh", TokenRefreshView.as_view()),
    path("verify", TokenVerifyView.as_view()),
    path("create-cuurent-user/", CreateUserView.as_view()),# only accounts who logged in can access this view!
    path("update-user/<int:pk>", UpdateUserView.as_view()),
    path("delete-user/<int:pk>", DeleteUserView.as_view()),#only admin will be able to delete accounts!
    
]

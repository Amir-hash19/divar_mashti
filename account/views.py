from django.shortcuts import render
from .models import UserAccount
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import UserAccountSerializer



class UserListView(ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer



class UserListCreateView(ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer




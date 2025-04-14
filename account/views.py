from .models import UserAccount
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView,DestroyAPIView
from .serializers import UserAccountSerializer, UserAccountSerializerD
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import status


class UserListView(ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer



class UserListCreateView(ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer


 
@api_view(["GET", "POST"])
def user_profile(request):
    if request.method == "GET":
        try:
            users = UserAccount.objects.all()  
        except UserAccount.DoesNotExist:
            return HttpResponse("No users found", status=404)  
            
        serializer_data = UserAccountSerializer(users, many=True) 
        return Response(serializer_data.data)

    elif request.method == "POST":
      
        serializer = UserAccountSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    


class CreateUserView(CreateAPIView):
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
            
        

class DeleteUserView(DestroyAPIView):
    serializer_class = UserAccountSerializerD
    queryset = UserAccount.objects.all()
    permission_classes = [IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message":"The User was Deleted Successfully!"}, status=status.HTTP_200_OK)
        



class UpdateUserView(UpdateAPIView):
    serializer_class = UserAccountSerializer
    queryset = UserAccount.objects.all()





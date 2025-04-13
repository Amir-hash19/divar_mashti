from .models import UserAccount
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import UserAccountSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



class UserListView(ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer



class UserListCreateView(ListCreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer



@api_view(["GET", "POST"])
def user_profile(request):
    user = UserAccount.objects.all()
    serializer_data = UserAccountSerializer(user, many=True)
    return Response(serializer_data.data)



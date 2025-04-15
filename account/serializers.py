from rest_framework.serializers import ModelSerializer
from .models import UserAccount



class UserAccountSerializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validated_data):
        user = UserAccount.objects.create_user(**validated_data)    
        return user
    

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance        
    




class UserAccountSerializerD(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"

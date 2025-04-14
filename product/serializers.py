from rest_framework.serializers import ModelSerializer
from .models import Product, Order
from rest_framework import serializers


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductDeleteSerializer(ModelSerializer):
    confirm_delete = serializers.BooleanField(write_only=True)
    class Meta:
        model = Order
        fields = ["confirm_delete", "customer", "status", "shipping_address", "total_price", "payment_status"]

    def validate(self, attrs):
        user = self.context['request'].user
        if user.instance.owner != user:
            raise serializers.ValidationError(" You are not allowed to delete this product!")
        if not attrs.get('confirm_delete'):
            raise serializers.ValidationError("For finishing this action we need your access!")
        return attrs    

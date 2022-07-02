from dataclasses import fields
from email.policy import default
from rest_framework import serializers
from .models import OrderItem, Menu, Table, Order

class tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class orderItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default=1)
    class Meta:
        model = OrderItem
        fields = "__all__"

class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"






# class CreateOrderSerializer(serializers.Serializer):
#     table = 
#     meal = serializers.ListField( child = serializers.ModelField() )
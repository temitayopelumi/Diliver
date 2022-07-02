from urllib import response
from django.shortcuts import get_object_or_404, render
import queue 
import threading
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Menu, Order, OrderItem
from .serializers import orderItemSerializer, menuSerializer


def get_order_object(orderId):
        try:
            return Order.objects.get(pk=orderId)
        except Order.DoesNotExist:
            raise Http404

class MenuList(APIView):
    """
    List all menu, or create a new  menu.
    """
    def get(self, request, format=None):
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = menuSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = menuSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        menu = self.get_object(pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddItemToOrder(APIView):
    def post(self, request, orderId):
        order = get_order_object(orderId)
        if order.status != "nyp":
            return Response({"status":400})
        # item = self.get_item_object(itemId)
        items = request.data["items"]
        if not isinstance(items, list):
            return Response({"message":"Bad Data, items should be a list"}, status=status.HTTP_400_BAD_REQUEST)
        for obj in items: 
            item_serializer = orderItemSerializer(data=obj)
            if item_serializer.is_valid():
               item_serializer.save()
               order.order_items.add(item_serializer.data["id"])
               order.save()
            else:
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"order":200})
        
class CreateOrder(APIView):
    def post(self, request, tableId):
        if Order.objects.filter(table_id=tableId, status="nyp").exists:
            return Response({"message":"Order Exists, kindly add items to this order."}, status=status.HTTP_400_BAD_REQUEST)
        order = Order.objects.create(table_id=tableId)
        items = request.data["items"]
        if not isinstance(items, list):
            return Response({"message":"Bad Data, items should be a list"}, status=status.HTTP_400_BAD_REQUEST)
        for obj in items: 
            item_serializer = orderItemSerializer(data=obj)
            if item_serializer.is_valid():
               item_serializer.save()
               order.order_items.add(item_serializer.data["id"])
               order.save()
            else:
                return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"order":200})

        
class PlaceOrder(APIView):
    def post(self, request, orderId):
        order = get_order_object(orderId)
        if order.status != "nyp":
            return Response( {"message":"Order has been Confirmed"},status=status.HTTP_400_BAD_REQUEST,)
        order.status="ac"
        order.save()
        return Response( {"message":"Order Confirmed"},status=status.HTTP_200_OK,)

preparation_queue = queue.Queue()

#only admin user can use this endpoint to confirm an order
class ConfirmOrder(APIView):
    permission_classes = (IsAdminUser)
    def post(self, request, orderId):
        order = get_order_object(orderId)
        if order.status != "ac":
            return Response({"status":400})
        order.status="preparing"
        order.save()
        preparation_queue.put(order.order_items)
        print(preparation_queue)
        return Response( {"message":"Order Confirmed"},status=status.HTTP_200_OK,)

from django.urls import path
from .views import MenuList, MenuDetail, AddItemToOrder, PlaceOrder, ConfirmOrder, CreateOrder


urlpatterns = [
    path("menu/", MenuList.as_view()),
    path("menu/<int:pk>/", MenuDetail.as_view(), name="menu-details"),
    path("add-item/<int:orderId>/", AddItemToOrder.as_view()),
    path("create-order/<int:tableId>/", CreateOrder.as_view()),
    path("place-order/<int:orderId>/", PlaceOrder.as_view()),
    path("confirm-order/<int:orderId>/", ConfirmOrder.as_view())
]
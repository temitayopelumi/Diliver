from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, UserManager

# Create your models here.


class Menu(models.Model):
    Meal_mode = (
        ("continental", "continental"),
        ("chinese", "chinese"),
        ("indian", "indian")
    )
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    modes = models.CharField(choices=Meal_mode, max_length=100)
    preparation_time = models.DurationField()

class Table(models.Model):
    table_number = models.IntegerField()
    description = models.CharField(blank=True, max_length=255)

class OrderItem(models.Model):
     item = models.ForeignKey(Menu, on_delete=models.CASCADE)
     quantity = models.IntegerField(default=1)

class Order(models.Model):
    Status = (
        ("completed", "Completed"),
        ("nyp", "Not Yet Placed"),
        ("preparing", "preparing"),
        ("ac" ,"Awaiting Confirmation"),
        ("rejected", "Rejected")

    )
    order_id = models.UUIDField(primary_key=False, default=uuid.uuid4, unique=True)
    table = models.ForeignKey(Table, related_name="table_order", on_delete=models.CASCADE)
    status = models.CharField(max_length=250, choices=Status, default="nyp")
    ordered_date = models.DateField(auto_now_add=True)
    order_items = models.ManyToManyField(OrderItem, related_name="order_item")
    total_waiting_time = models.FloatField(blank = True, null=True)
    total_amount = models.FloatField(blank=True, null=True)


#assuming you cannot remove from an order or add to it.
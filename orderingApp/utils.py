from orderingApp.serializers import CalculateItemSerializers


def calculate(order):
    price = 0
    max_time = 0
    for orderItem in order.order_items.all():
        data = CalculateItemSerializers(orderItem).data
        quantity = data['quantity']
        price += quantity * data["item"]["price"]
        if data["item"]["total_seconds"] > max_time:
            max_time = data["item"]["total_seconds"]
    order.total_amount = price
    order.total_waiting_time = max_time
    order.save()
## An application for a taking orders from a restaurant that has 3 meal modes - continental, Chinese and Indian for dine in experience. 


### Entity Relation Diagram.

![alt text](https://github.com/temitayopelumi/Diliver/blob/main/output.png?raw=true)




### How it works
Assumptions: All items ordered by a customer or table will be proccessed at the same time. i.e the waiting time of the order is equal to highest waiting time of the items order

Customer side

View Menu List

Addon
Get to know the add on details of a particular food acutely before placing your order.

Create Order
Create order using your table number, you can create an order while taking your time. The table number is an identifier.

Add Items to Order
You can add item to  an order.

Place Order: 
once you are statisfied with the order, the order can be placed. The order is will be place on awiting confirmation

Confirm Order:
This is done by an admin user, the order is examined, and confirmed. The order will be added to the preparation queue.

Order Status
This feature empowers the restaurant to check the current status and progress of the order.


Admin

Menu
Add and edit menus

Confirm Order

Give bill:
Once the order has been completed , the bill will calulated and displayed to the user.

Close the order:
Paid order will be closed

## Internal Workings

### Tools used
1. Python 
2. Django and Django Rest Framework

### 

Once an order has placed and confirm , it enters a preparation queue. The total wait time for order is the highest preparation time for an order item. Multithreading is used. Order Items i.e Meals is further added to a queue. once an item is beign preparaed, the process jumps another thread. till the order items of a particular order is completed and the order is completed and delivered.


If there is a delay, the wait time is increased by 15mins.

Orders can be cancelled if they are not yet completed.

Completed orders will rejected. and bill cancelled for such customers.

Tables can join together to make an order. Check Entiy Relation diagram



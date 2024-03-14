from django.db import models
from customers.models import customer
from products.models import Products

# Create your models here.


class CartOrder(models.Model):
    status_chices = (
         ('1','order_confirmed'),
         ('2','order_processed'),
         ('3','order_delivered'),
         ('4','order_rejected'),
         ('0','cart_stage')
     )   
    del_choices = (
            ('0','delete'),
            ('1','live')
    )
    order_status = models.IntegerField(choices=status_chices,default=0)
    owner= models.ForeignKey(customer, on_delete=models.SET_NULL, related_name='orders',null=True)
    del_status = models.IntegerField(choices=del_choices,default=1)
    creat_at = models.DateTimeField(auto_now_add=True)
    updat_at = models.DateTimeField(auto_now=True)

class OrderedItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, related_name='added_carts',null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(CartOrder,on_delete=models.CASCADE,related_name='added_items')
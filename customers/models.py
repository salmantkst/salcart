from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# model for the customer
    
class customer(models.Model):
    del_choices = (
            ('0','delete'),
            ('1','live')
    )
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=13)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    del_status = models.IntegerField(choices=del_choices,default=1)
    creat_at = models.DateTimeField(auto_now_add=True)
    updat_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
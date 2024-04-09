from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Customer(models.Model):

    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    

    def __str__(self):

        return self.user.first_name

class Employee(models.Model):

    id  = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user.first_name


class Product(models.Model):

    prod_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):

        return self.name
    
class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=100, default="Cash")
    created_at = models.DateTimeField(auto_now_add=True)



    



from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title=models.CharField(max_length=64)
    description=models.CharField(max_length=128)
    bid=models.PositiveIntegerField()
    account = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    categories = (
        ("fashion","Fashion"),
        ("toys","Toys"),
        ("electronics","Electronics"),
        ("home","Home")
    )
    category =models.CharField(max_length=64,choices=categories)
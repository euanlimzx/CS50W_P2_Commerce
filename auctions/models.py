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

class Watchlist(models.Model):
    watchlister = models.ForeignKey(User,on_delete=models.CASCADE,related_name="watchlister")
    watchlisting = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="watchlisting")

class Bid(models.Model):
    bidvalue = models.PositiveIntegerField()
    bidder= models.ForeignKey(User,on_delete=models.CASCADE,related_name="bidlister")
    bidlisting = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="bidlisting")

class Win(models.Model):
    winlisting=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="winlisting")
    winner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="winner")

class Comment(models.Model):
    commentlisting=models.ForeignKey(Listing,on_delete=models.CASCADE,related_name="commentlisting")
    comment=models.CharField(max_length=300)
    commenter=models.ForeignKey(User,on_delete=models.CASCADE,related_name="commenter")
    date=models.DateTimeField(auto_now=True)
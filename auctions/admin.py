from django.contrib import admin
from .models import User,Listing,Watchlist

# Register your models here.
admin.site.register(User)
admin.site.register(Watchlist)
admin.site.register(Listing)
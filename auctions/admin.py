from django.contrib import admin
from .models import Bid, User,Listing,Watchlist,Bid,Win

# Register your models here.
admin.site.register(User)
admin.site.register(Watchlist)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Win)
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .forms import ListingForm
from .models import User,Listing,Watchlist
from .models import User


def index(request):
    return render(request, "auctions/index.html",{
        "listings":Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        listing=ListingForm(request.POST)
        if listing.is_valid():
            listing.instance.account = request.user
            listing.save(commit=False)
            listing.save()
            return HttpResponseRedirect(reverse("listing",args=(listing.instance.id,)))
        else:
            messages.error(request,"error")
    else:
        listing = ListingForm()
        return render(request,"auctions/create.html",{
        "listing":listing})

@login_required
def listing(request,listing_id):
    listing = Listing.objects.get(pk=listing_id)
    user = request.user
    if request.method == "POST":
        if 'watchlist' in request.POST:
            if Watchlist.objects.filter(watchlisting=listing,watchlister=user).exists():
                object=Watchlist.objects.get(watchlisting=listing,watchlister=user)
                object.delete()
            else:
                object=Watchlist(watchlisting=listing,watchlister=user)
                object.save()
        if 'bid' in request.POST:
            newbid=request.POST["newbid"]
            listing.bid=newbid
            listing.save()
        return HttpResponseRedirect(reverse('listing',args=(listing_id,)))
    else:    
        try:
            object = Watchlist.objects.get(watchlisting=listing,watchlister=user)
            watchlist=[]
            watchlist.append(object)
        except Watchlist.DoesNotExist:
            watchlist=[]
        return render(request,"auctions/listing.html",{
            "listing":listing,
            "watchlist":watchlist
        })

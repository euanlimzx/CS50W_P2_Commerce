from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        description = forms.CharField(widget=forms.Textarea)
        fields=("title","description","bid","category")
        
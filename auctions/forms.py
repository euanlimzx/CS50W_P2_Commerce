from django import forms
from .models import Listing,Comment
from django.forms import Textarea

class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        description = forms.CharField(widget=forms.Textarea)
        fields=("title","description","bid","category")
        widgets = {
            'description': Textarea(attrs={'class':'form-control','cols': 20, 'rows': 10}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        comment =forms.CharField(widget=forms.Textarea)
        fields=("comment",)
        widgets = {
            'comment': Textarea(attrs={'class':'form-control','cols': 20, 'rows': 10}),
        }

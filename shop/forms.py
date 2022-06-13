from django import forms
from .models import review ,clothe

class ReviewForm(forms.ModelForm):
    class Meta:
        model=review
        fields=['Your_review','name','email']


class ClotheForm(forms.ModelForm):
    class Meta:
        model=clothe
        fields='__all__' 
        exclude=('owner','slug',)
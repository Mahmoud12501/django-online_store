from django import forms
from .models import Send_Message

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Send_Message
        fields=['email','massage']
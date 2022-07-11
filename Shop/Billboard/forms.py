from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Ad, Echo



class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            "ad_theme",
            "text_of_ad",
            "categoryAd",
            "upload_file",
            "upload_image",
        ]

class EchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = [
            "echo_text",
            # "echo_ad",
        ]
from django import forms

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
        ]
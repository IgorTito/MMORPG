import django.forms
from django_filters import FilterSet, DateTimeFilter
from .models import Ad


class AdFilter(FilterSet):
    date_of_create = DateTimeFilter(lookup_expr="gte", widget=django.forms.DateInput(attrs={"type": "date"}))

    class Meta:

        model = Ad
        fields = {
           'ad_theme': ['icontains'],
           'categoryAd': ['exact']
        }


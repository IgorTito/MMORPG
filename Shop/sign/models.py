from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  )

    def save(self, commit=True):
        user = super(BaseRegisterForm, self).save()
        main_group = Group.objects.get(name='creators')
        main_group.user_set.add(user)
        return user


class BaseSignupForm(SignupForm):
    def save(self, request):
        user = super(BaseSignupForm, self).save(request)
        main_group = Group.objects.get(name='creators')
        main_group.user_set.add(user)
        return user
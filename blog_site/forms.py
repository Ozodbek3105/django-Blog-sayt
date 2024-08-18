from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404


class RegistrationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ['username', 'email']
      

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Parollar mos emas.")
        return password2
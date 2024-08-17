from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404


class RegistrationForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

    def clean_email(self):
        email = self.cleaned_data["email"]
        # id = self.instance.id
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already in use")
        
        else:
            return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Parollar mos emas.")
        return password2
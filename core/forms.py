from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from core.models import State
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    # this is not port of model that is why write it before meta class
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User

        fields = ['username',
                  'first_name',
                  'last_name',
                  'email']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))

    password = forms.CharField(
        label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))


class AddState(forms.ModelForm):
    class Meta:
        model = State
        fields = ['title', 'desc', 'pic']
        labels = {
            'title': "Title",
            "Desc": "Description",
            'pic': ""
        }
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "desc": forms.Textarea(attrs={'class': 'form-control'}),

        }

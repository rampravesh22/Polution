# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# from django import forms
# from core.models import State
# from django.contrib.auth.models import User
# from django.utils.translation import gettext, gettext_lazy as _


# class SignUpForm(UserCreationForm):
#     # this is not port of model that is why write it before meta class
#     password1 = forms.CharField(
#         label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder":"Password"}))

#     password2 = forms.CharField(
#         label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control',"placeholder":"Confirm Password"}))

#     class Meta:
#         model = User

#         fields = ['username',
#                   'email',
#                   ]

#         labels = {
#             'email': 'Email'
#         }

#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Username"}),
#             # 'first_name': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Username"}),
#             # 'last_name': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Username"}),
#             'email': forms.TextInput(attrs={'class': 'form-control',"placeholder":"Email"})
#         }


# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(
#         attrs={'autofocus': True, 'class':"","placeholder":"Username"}))

#     password = forms.CharField(
#         label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': '',"placeholder":"Password"}))


# class AddState(forms.ModelForm):
#     class Meta:
#         model = State
#         fields = ['title', 'desc', 'pic']
#         labels = {
#             'title': "Title",
#             "Desc": "Description",
#             'pic': ""
#         }
#         widgets = {
#             "title": forms.TextInput(attrs={'class': 'form-control'}),
#             "desc": forms.Textarea(attrs={'class': 'form-control'}),

#         }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import SetPasswordForm
from custom_user.models import User


class SignUpForm(UserCreationForm):
    user_name = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={"class": "form-control style", "placeholder": "Username"}))
    email = forms.EmailField(label='Email Id', max_length=254, help_text='Email.',
                             widget=forms.TextInput(attrs={"class": "form-control style", "placeholder": "Email"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"class": "form-control style", "placeholder": "Password"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={"class": "form-control style", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = (
            'user_name',
            'email',
            'password1',
            'password2'
        )



class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control borders", 'type': "Password", 'placeholder': "Current Password"}))
    new_password1 = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control borders", 'type': "Password", 'placeholder': "New Password"}))
    new_password2 = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control borders", 'type': "Password", 'placeholder': "Confirm Password"}))

# class UserPasswordSet(SetPasswordForm):
#     # username = forms.CharField(label='Username', widget=forms.TextInput(
#     #     attrs={"class": "form-control style", "placeholder": "USERNAME"}))
#     password_set = forms.CharField(widget=forms.TextInput(
#         attrs={"class": "form-control borders", 'type': "Password", 'placeholder': "Set Password"}))
#   class ForgotForm(UserCreationForm):
#     email = forms.EmailField(label='Email Id', max_length=200)
#     password = forms.PasswordInput()

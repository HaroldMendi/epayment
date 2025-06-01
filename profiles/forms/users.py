from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Username"}), label=False)
    email = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Email", 'type': 'email'}), label=False)
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Password"}), label=False)
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"placeholder": "Confirm password"}), label=False)

class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username,' 'password']

    username = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Username"}), label=False)
    password = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Password", "type":"password"}), label=False)
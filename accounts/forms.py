from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Transaction
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.shortcuts import render, redirect

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    first_name=forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    last_name=forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model= User
        fields=['username','first_name','last_name','email', 'password1','password2']

class TransactionForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        self.fields['payee'].queryset = User.objects.exclude(id=user.id)

    
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'category','payee', 'payment_method', 'reference_number','attachments']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'payee': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control'}),
            'attachments': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        


        
# class LoginForm(AuthenticationForm):
#     first_name = forms.CharField(widget=TextInput())
#     last_name = forms.CharField(widget=TextInput())
#     email = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())
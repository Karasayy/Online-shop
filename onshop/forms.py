from django import forms
from .models import Product
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(ModelForm):

	required_css_class = 'required'
	class Meta:
		model = Product
		fields = ('__all__')



class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2')
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-input'}),
			'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
			'password2': forms.PasswordInput(attrs={'class': 'form-input'})
		}

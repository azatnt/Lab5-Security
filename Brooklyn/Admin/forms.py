from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *




class UserRegisterForm(UserCreationForm):
	# email = forms.EmailField()
	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ("Пароль")})
		self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': ("Подтвердите")})


	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
		widgets = {
		 'username':forms.TextInput(attrs = {'placeholder': 'Никнейм'}),
		 'email':forms.TextInput(attrs = {'placeholder': 'Email'}),
		 # 'password1' : forms.PasswordInput(attrs = {'placeholder': 'Password'}),
		 # 'password2':forms.TextInput(attrs = {'placeholder': 'Подтвердите'})
		}


		help_texts={
			'username': None
		}


# class UpdateDetailsForm(forms.ModelForm):
# 	class Meta:
# 		model = Csv
# 		fields = ('file_name', )


# class ClientDetailsForm(forms.ModelForm):
#     issue_date = DateField(input_formats=settings.DATE_INPUT_FORMATS)
#     class Meta:
#        model = TDebtData

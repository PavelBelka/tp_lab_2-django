from django import forms

class AuthForm(forms.Form):
	login = forms.CharField(label = 'Логин')
	password = forms.CharField(label = 'Пароль')
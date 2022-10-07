from this import d
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserForm(forms.ModelForm):
	username = forms.CharField(max_length=100)
	email = forms.EmailField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	password_confirmation = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'password_confirmation')

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Username already exists')
		return username
	
	def clean_email(self):
		data = self.cleaned_data["email"]
		if User.objects.filter(email=data).exists():
			raise forms.ValidationError("Email already exists")
		return data
	

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		password_confirmation = cleaned_data.get("password_confirmation")

		if password != password_confirmation:
			raise forms.ValidationError("password and password_confirmation does not match")

	def clean_password(self):
		password = self.cleaned_data.get('password')
		if len(password) < 6:
			raise forms.ValidationError('Password must be at least 6 characters')
		return password


class LoginUserForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError('Username does not exist')
		return username

	def clean_password(self):
		password = self.cleaned_data.get('password')
		username = self.cleaned_data.get('username')
		user = User.objects.get(username=username)
		if not user.check_password(password):
			raise forms.ValidationError('Password is incorrect')
		return password


	

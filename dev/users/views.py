from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from users.forms import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


User = get_user_model()

def register(request):
	if request.user.is_authenticated:
		return redirect('/')
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = User(
				username = form.cleaned_data.get('username'),
				email = form.cleaned_data.get('email'),
			)
			user.set_password(form.cleaned_data.get('password'))
			user.save()
			return redirect('login')
		
	else:
		form = CreateUserForm()
	return render(request, 'register.html', {'form': form})

def login(request):
	if request.method == 'POST':
		form = LoginUserForm(request.POST)
		if form.is_valid():
			user = User.objects.filter(username=form.cleaned_data.get('username')).first()
			auth_login(request, user)
			return redirect('/')
	else:
		form = LoginUserForm()
	return render(request, 'login.html', {'form': form})

def logout(request):
	if request.user.is_authenticated:
		auth_logout(request)
		return redirect('login')
		

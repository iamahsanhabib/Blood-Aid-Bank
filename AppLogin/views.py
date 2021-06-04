from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from AppLogin.forms import UserProfileChange

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usernames = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usernames, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
    return render(request, 'AppLogin/login.html', context={'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def user_profile(request):
    return render(request, 'AppLogin/profile.html', context={})

@login_required
def change_user_profile(request):
    current_user = request.user
    form = UserProfileChange(instance = current_user)
    if request.method == 'POST':
        form  = UserProfileChange(request.POST, instance = current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance = current_user)
            return redirect('/account/profile/')
    return render(request, 'AppLogin/change_profile.html', context={'form': form})

@login_required
def change_user_password(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    changed = False
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'AppLogin/change_password.html', context={'form': form, 'changed': changed})        


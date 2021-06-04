from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
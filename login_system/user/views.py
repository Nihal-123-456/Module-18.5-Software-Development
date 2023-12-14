from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.forms import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'base.html')

def user_signup(request):
    if request.user.is_authenticated is False:
        if request.method == 'POST':
            form = signup(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
        else:
            form = signup()
    
        return render(request, 'signup.html', {'form': form,'type':'register'})
    else:
        return redirect('user_profile')

def user_login(request):
    if request.user.is_authenticated is False:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Logged in successfully')
                    return redirect('user_profile')
                else:
                    messages.warning(request, 'Wrong information')
                    return redirect('user_login')
        else:
            form = AuthenticationForm()
    
        return render(request, 'signup.html', {'form': form,'type':'Login'})
    else:
        return redirect('user_profile')

@login_required
def user_profile(request):
        return render(request,'profile.html',{'user':request.user})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')

@login_required
def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request, 'Password changed successfully')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('user_profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'pass_change.html',{'form':form})

@login_required
def change_password2(request):
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                messages.success(request, 'Password changed successfully')
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('user_profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request,'pass_change.html',{'form':form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import customUserCreationForm
from django.contrib.auth.decorators import login_required
from auth_app.forms import UserRegistrationForm

# Vue pour l'inscription
def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('index')
    else :
        form = UserRegistrationForm()
    return render(request,'register.html',{'form' : form})

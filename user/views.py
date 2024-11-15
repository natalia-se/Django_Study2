from django.shortcuts import render, redirect
from .models import User
from user import forms
from django.contrib import messages

def welcome(request):
    return render(request, 'user/welcome.html')

def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }

    return render(request, 'user/user.html', context)

def form(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            form.save() 
            print("Validation success!")
            print("Data saved to the database.")
            messages.success(request, "Your form has been submitted successfully!")
            return redirect('welcome')
        else:
            messages.error(request, "There was an error with your submission.")

    return render(request, "user/form.html", {"form": form})
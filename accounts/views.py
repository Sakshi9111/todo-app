from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm


def signup_view(request):
    """
    Handle user registration/signup
    Login and Logout are handled by Django's built-in views
    """
    # Redirect if user is already logged in
    if request.user.is_authenticated:
        return redirect('todo_list')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Success message
            messages.success(request, f'Welcome {username}! Your account has been created successfully.')
            
            # Automatically log in the user after signup
            login(request, user)
            
            # Redirect to todo list
            return redirect('todo_list')
        else:
            # Show error if form is invalid
            messages.error(request, 'Please correct the errors below.')
    else:
        # GET request - show empty form
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

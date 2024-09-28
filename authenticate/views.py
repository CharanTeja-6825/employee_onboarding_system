from django.contrib.auth import authenticate, login
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .forms import RegistrationForm

# Create your views here.
def homepage(request):
    return render(request, 'base.html')


def custom_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if the username starts with 'admin@' and has length 10
        if username.startswith('admin@') and len(username) == 10:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:  # Ensure it's an admin account
                    login(request, user)
                    return redirect('admin_dashboard')  # Change this to the actual admin URL
            else:
                return HttpResponse("Invalid admin credentials.")

        # Check if the username length is 10 (Employee)
        elif len(username) == 10:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_dashboard')  # Change to employee dashboard URL
            else:
                return HttpResponse("Invalid employee credentials.")

        # Check if the username length is 4 (Mentor)
        elif len(username) == 4:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mentor_dashboard')  # Change to mentor dashboard URL
            else:
                return HttpResponse("Invalid mentor credentials.")

        else:
            return HttpResponse("Invalid login conditions.")
    else:
        return render(request, 'login.html')  # Login template


def generate_employee_id():
    return str(random.randint(1000000000, 9999999999))  # 10-digit ID for employee

def generate_mentor_id():
    return str(random.randint(1000, 9999))  # 4-digit ID for mentor

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Generate username based on role
            if role == 'employee':
                username = generate_employee_id()  # 10-digit ID
            else:  # role == 'mentor'
                username = generate_mentor_id()  # 4-digit ID

            # Create and save the user
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=make_password(password),
            )

            # You can also store the role in the user profile if necessary
            # e.g., user.profile.role = role

            return HttpResponse(f"User registered successfully! Your username is {username}")
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

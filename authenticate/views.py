from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

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

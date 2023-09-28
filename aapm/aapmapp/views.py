from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import dealer
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def homelogin(request):
    return render(request, 'homelogin.html')


def register(request):
    if request.method == 'POST': 
        fullname = request.POST['fullname']
        username = request.POST['username']
        phoneno  = request.POST['phone']
        housename = request.POST['housename']
        pincode = request.POST['pincode']
        district = request.POST['district']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        # Create a user instance but do not save it yet
        user = dealer(username=username, email=email)

        # Set the password for the user
        user.set_password(password)

        # Save the user to the database
        user.save()

        # Redirect to the home page or any desired page
        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!!')

    return render(request, 'login.html')

'''def register2(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'register2.html', {'error_message': 'Passwords do not match'})

        # Create a user instance but do not save it yet
        user = customer(username=username, email=email)

        # Set the password for the user
        user.set_password(password)

        # Save the user to the database
        user.save()

        # Redirect to the home page or any desired page
        return redirect('login2')

    return render(request, 'register2.html')

def user_login2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!!')

    return render(request, 'login2.html')'''

def user_logout(request):
    logout(request)
    return redirect('home')

'''def user_logout2(request):
    logout(request)
    return redirect('home')'''


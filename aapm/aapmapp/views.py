from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import dealer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login



#for activating user account
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.template.loader import render_to_string
from django.urls import NoReverseMatch,reverse
# Create your views here.

#email
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.mail import BadHeaderError,send_mail
from django.core import mail
from django.conf import settings
from django.core.mail import EmailMessage

#threading
import threading

#reset passwor generater
from django.contrib.auth.tokens import PasswordResetTokenGenerator
# Create your views here.


def homelogin(request):
        return render(request, 'homelogin.html')



def register(request):
    if request.method == 'POST': 
        fullname = request.POST['fullname']
        username = request.POST['username']
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        # Create a user instance but do not save it yet
        user = dealer(username=username, email=email,role=role ,fullname=fullname,)

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
            request.session['role'] = user.role
            if user.username == "admin" and user.password == "admin" :
                return redirect('admin_dashboard')
            else:
                return redirect('userloginhome')
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
    if request.user.is_authenticated:
        logout(request)
    return redirect('userloginhome')

@login_required(login_url='login')
def userloginhome(request):
    return render(request,'userloginhome.html')




'''def user_logout2(request):
    logout(request)
    return redirect('home')'''

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def users(request):
    # Query the database to get the data you want to display on the admin dashboard
    dealers = dealer.objects.all()  # You can adjust this queryset based on your requirements
    # You can fetch other data in a similar way

    # Pass the data to the template context
    context = {
        'dealers': dealers,
        # Add other data you want to pass to the template
    }
    
    return render(request, 'users.html', context)

       








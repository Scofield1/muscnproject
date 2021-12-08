from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .my_captcha import FormWithCaptcha
from .forms import ContactForm, SubscribersForm


def index(request):
    form = SubscribersForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)

def membership(request):
    return render(request, 'membership.html', {})

def shop(request):
    return render(request, 'shop.html', {})

def mission(request):
    return render(request, 'mission.html', {})

def visionary(request):
    return render(request, 'visionary.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent Successfully')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
def register(request):
    context = {
        'captcha': FormWithCaptcha
    }
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username has been taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password Doesn't match")
            return redirect('register')
    else:
        return render(request, 'register.html', context)

def login(request):
    context = {
        'captcha': FormWithCaptcha
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Message Sent Successfully')
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Information')
            return redirect('login')
    else:
        return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')

def dashboard(request, name):
    profile = User.objects.get(name=name)
    context = {
        'profile': profile
    }
    return render(request, 'dashboard.html', profile)

def subscriber(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('subscriber')
    else:
        form = SubscribersForm()
    context = {
        'form': form
    }
    return render(request, 'subscriber.html', context)
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def home(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None: #checking if the authenticate returns correct or incorrectf
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.success(request, "Login Failed")
            return redirect('home')
    return render(request, 'home.html', {})
#POST → redirect('home') → 
# browser makes a new GET to / → r
# ender(request, 'home.html', {}) runs.

#{} is the template context dict — 
# the variables you pass into the template. 
# Keys become template variables. 
# If empty, no extra variables are passed 
# (context processors like request/user/messages still run).


def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successful")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #is a dict (available after form.is_valid()) 
            # containing the form's validated and converted field values.
            #form.cleaned_data converts raw request.POST strings into the 
            # appropriate Python types 
            # (e.g. '30' → 30 int, '2026-03-05' → datetime.date); 
            # only text fields (username/password) remain strings.
            user = authenticate(username=username, password = password)
            login(request, user)
            messages.success(request, "registered successfully")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})
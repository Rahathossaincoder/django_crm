from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordFrom
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()

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
    return render(request, 'home.html', {'records':records})
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

def customer_record(request, pk):#this pk aka primary key is coming from urls
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You have to login to see this page")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "Need to login to do this")
        return redirect('home')
    
def add_record(request):
    form = AddRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            add_record = form.save()
            messages.success(request, "Successfully saved the record")
            return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "Request added...")
        return redirect('home')
    
def update_record(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordFrom(request.POST or None, instance=current_record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record updated successfully")
                return redirect('home')
        return render(request, 'update_record.html', {'form': form, 'record': current_record})
    else:
        messages.success(request, "You must be logged in...")
        return redirect('home')


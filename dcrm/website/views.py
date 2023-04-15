from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from .forms import SignUpForm, AddRecordForm, newSecret
from .models import Record, secretClient


# Create your views here.
def home(request):
    records = Record.objects.all()


    # Check to see if logging in
    if request.method =='POST':
        username = request.POST['username'] # name of the field in the form
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request,user)
                messages.success(request,"You are logged in")
                return redirect('home')
        else:
            messages.success(request,"There is an error")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})


#def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out...")
    return redirect('home')

def xxx(request):
    return HttpResponse("Hello")

def welcome(request):
    return render(request,"welcome.html",{'today':datetime.today})

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,"You have sucessfully registered..")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in to view that page..")
        redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Records Deleted Sucessfully")
        redirect('home')
    else:
        messages.success(request,"must be admin bro")
        return redirect('home')

def add_record(request):
    #if request.user.is_authenticated:
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Recorded added")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request,"must be logged in")
        return redirect('home')

    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated")
            return redirect('home')
        return render(request,'update_record.html', {'form':form})
    else:
        messages.success(request,"must be logged in")
        return redirect('home')

def secretClients(request):
    allSecrets = secretClient.objects.all()
    return render(request,"secretClients.html",{'allSecrets':allSecrets})

def secretRecord(request, pk):
    secretRecord = secretClient.objects.get(id=pk)
    return render(request,"secretRecord.html",{'secretRecord':secretRecord})
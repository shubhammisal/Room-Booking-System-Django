from django.shortcuts import render , redirect
from django.contrib import messages
from booking.forms import Add_Customer,Add_Room,Book,Pay
import csv
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'booking/home.html')

def AddCustomer(request):
    if request.method == 'POST':
        form  = Add_Customer(request.POST)
        if form.is_valid():
            user=form.save()
            with open("Customer_Data.csv", 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow(form.cleaned_data)
            messages.success(request, "Customer Data Added successfuly." )
            request.session['name'] = form.cleaned_data['name']
            return redirect("book_room")
        messages.error(request, "Invalid information.")
    form = Add_Customer()
    return render(request,'booking/add_customer.html',{'form':form})

def AddRoom(request):
    if request.method == 'POST':
        form  = Add_Room(request.POST)
        if form.is_valid():
            user=form.save()
            with open("Rooms_Data.csv", 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow(form.cleaned_data)
            messages.success(request, "Room Added successful." )
            return redirect("home")
        messages.error(request, "Invalid information.")
    form = Add_Room()
    return render(request,'booking/add_room.html',{'form':form})

def BookRoom(request):
    if request.method == 'POST':
        form  = Book(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.name=request.session['name'] 
            user.save()
            with open("Booking_Data.csv", 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow(form.cleaned_data)
            messages.success(request, "Booking successful." )
            return redirect("payment")
        messages.error(request, "Invalid information.")
    form = Book()
    return render(request,'booking/booking.html',{'form':form})

def Payment(request):
    if request.method == 'POST':
        form  = Pay(request.POST)
        if form.is_valid():
            user=form.save()
            with open("Payment_Data.csv", 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow(form.cleaned_data)
            messages.success(request, "data Added successful." )
            return redirect("home")
        messages.error(request, "Invalid information.")
    ini_data={
        'name':request.session['name']
    }
    form = Pay(initial=ini_data)
    form.data['name']=request.session['name']
    return render(request,'booking/payment.html',{'form':form})


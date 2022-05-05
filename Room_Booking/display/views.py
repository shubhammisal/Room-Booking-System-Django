from distutils.sysconfig import customize_compiler
from django.db.models import Sum
from django.shortcuts import render
from datetime import date
from booking.models import Booking, Customer, Payment, Rooms

def Display_Customer(request):
    if request.method == 'POST':
        n=request.POST["search"]
        data=Customer.objects.filter(name__contains=n)
        cus = {"cus": data}
        return render(request,'display/display_customer.html',cus)
    data = Customer.objects.all()
    cus = {"cus": data}
    return render(request,'display/display_customer.html',cus)

def Display_Rooms(request):
    if request.method == 'POST':
        n=request.POST["search"]
        data=Rooms.objects.filter(room_no=n)
        cus = {"cus": data}
        return render(request,'display/display_rooms.html',cus)
    data = Rooms.objects.all()
    cus = {"cus": data}
    return render(request,'display/display_rooms.html',cus)

def Display_Booking(request):
    if request.method == 'POST':
        n=request.POST["search"]
        data=Booking.objects.filter(name__contains=n)
        cus = {"cus": data}
        return render(request,'display/display_booking.html',cus)
    data = Booking.objects.all()
    cus = {"cus": data}
    return render(request,'display\display_booking.html',cus)


def Display_Payment(request):
    if request.method == 'POST':
        n=request.POST["search"]
        data=Payment.objects.filter(name__contains=n)
        cus = {"cus": data}
        return render(request,'display/display_payment.html',cus)
    data = Payment.objects.all()
    cus = {"cus": data}
    return render(request,'display\display_payment.html',cus)

def Summary(request):
    n=Customer.objects.count()
    n1=Booking.objects.count()
    n2=Payment.objects.count()
    data={}
    data['trecord']=n
    data['tbooking']=n1
    data['tpay']=n2
    month=date.today().month
    a1=Payment.objects.filter(Payment_date__month=month).aggregate(Sum('amount'))
    data['tpayment']=a1['amount__sum']
    a2=Payment.objects.filter(Payment_date__month=month-1).aggregate(Sum('amount'))
    data['lastpay']=a2['amount__sum']
    a3=Payment.objects.aggregate(avg=Sum('amount'))
    data['avgpay']=a3['avg']
    return render(request,'display\summary.html',{"data":data})

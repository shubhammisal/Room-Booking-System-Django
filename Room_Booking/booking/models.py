from django.db import models
from django.forms import Widget


class Customer(models.Model):
    GENDER = (('M', 'Male'),
        ('F', 'Female'),)
    name=models.CharField(max_length=30)
    Gender=models.CharField(max_length=1,choices=GENDER,default="Male")
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=12)
    adhar_no=models.CharField(max_length=20)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Rooms(models.Model):
    TYPE=(("AC","AC"),("Non-AC","Non-AC"))
    room_no=models.CharField(max_length=50)
    room_type=models.CharField(max_length=50,choices=TYPE,default="Non-AC")
    is_available=models.BooleanField(default=True)
    price=models.FloatField(default=1000.00)

    def __str__(self):
        return self.room_no

class Booking(models.Model):
    room_no=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    # name=models.ForeignKey(Customer, on_delete=models.CASCADE)
    Check_In_day=models.DateField()
    Check_Out_day=models.DateField()
    amount=models.FloatField()

class Payment(models.Model):
    PTYPE=(("Cash","Cash"),("Online","Online"))
    name=models.CharField(max_length=100)
    # name=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Payment_Type=models.CharField(max_length=50,choices=PTYPE,default="Cash")
    amount=models.FloatField()
    Payment_date=models.DateField()

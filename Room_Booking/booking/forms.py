from dataclasses import field

from django import forms
from booking.models import Customer
from booking.models import Rooms
from booking.models import Booking,Payment

class Add_Customer(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class Add_Room(forms.ModelForm):
    class Meta:
        model=Rooms
        fields="__all__"

class Book(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        widgets = {
                'Check_In_day': forms.DateInput(attrs={'type': 'date'}),
                'Check_Out_day':forms.DateInput(attrs={'type': 'date'})}
        exclude =('name',)

class Pay(forms.ModelForm):
    class Meta:
        model=Payment
        fields="__all__"
        widgets = {
            'Payment_date': forms.DateInput(attrs={'type': 'date'})
        }
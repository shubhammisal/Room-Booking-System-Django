"""Room_Booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from booking import views
from login import views as v1
from display import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',v1.login,name='login'),
    path('logout',v1.logout,name='logout'),
    path('home',views.home,name="home"),
    path('add_customer',views.AddCustomer,name="add_customer"),
    path('add_room',views.AddRoom,name="add_room"),
    path('book_room',views.BookRoom,name="book_room"),
    path('payment',views.Payment,name="payment"),
    path('display_customer',v2.Display_Customer,name='display_customer'),
    path('display_rooms',v2.Display_Rooms,name='display_rooms'),
    path('display_booking',v2.Display_Booking,name='display_booking'),
    path('display_payment',v2.Display_Payment,name='display_payment'),
    path('summary',v2.Summary,name='summary'),
]

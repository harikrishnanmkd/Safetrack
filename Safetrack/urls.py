"""untitled URL Configuration

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

from Safetrack import views

urlpatterns = [
    path('login/', views.login),
    path('login_post/', views.login_post),
    path('Studentregistration/', views.Studentregistration),
    path('Studentregistration_post/', views.Studentregistration_post),
    path('Editstudent/<id>', views.Editstudent),
    path('Editstudent_POST/', views.Editstudent_POST),
    path('Driverregistration/', views.Driverregistration),
    path('DriverRegistration_Post/', views.DriverRegistration_Post),
    path('Editdriver/<id>', views.Editdriver),
    path('Editdriver_POST/', views.Editdriver_POST),
    path('Viewdriver/',views.Viewdriver),
    path('Searchdriver/',views.Searchdriver),
    path('Viewstudent/',views.Viewstudent),
    path('Viewstudent_post/',views.Viewstudent_post),
    path('delete_student/<id>', views.delete_student),
    path('delete_driver/<id>', views.delete_driver),
    path('admin_home/',views.admin_home),
    path('Busregistration/', views.Busregistration),
    path('BusRegistration_Post/', views.Busregistration_Post),
    path('Viewbus/', views.Viewbus),
    path('Viewbus_POST/',views.Viewbus_POST),
    path('delete_bus/<id>', views.delete_bus),
    path('Editbus/<id>', views.Editbus),
    path('Editbus_POST/', views.Editbus_POST),
    path('Addroute/', views.Addroute),
    path('Addroute_POST/', views.Addroute_POST),
    path('sendpaymentnotification/', views.sendpaymentnotification),
    path('sendpaymentnotification_POST/', views.sendpaymentnotification_POST),
    path('viewpaymentnotification/', views.viewpaymentnotification),
    path('viewpaymentnotification_POST/', views.viewpaymentnotification_POST),
    path('Viewroute/', views.ViewRoute),
    path('ViewRoute_POST/',views.ViewRoute_post),
    path('Editroute/<id>', views.Editroute),
    path('Editroute_POST/', views.Editroute_POST),
    path('delete_route/<id>', views.delete_route),
    path('Allocation/<id>', views.Allocationsb),
    path('Allocation_POST/', views.Allocation_POST),
    path('Viewallocation/', views.Viewallocation),
    path('Viewallocation_POST/',views.Viewallocation_post),
    path('Editallocation/<id>', views.Editallocation),
    path('Editallocation_POST/', views.Editallocation_POST),
    path('delete_allocation/<id>', views.delete_allocation),
    path('delete_paymentnotification/<id>', views.delete_paymentnotification),
    path('makefeepayment_POST/', views.makefeepayment_POST),
    path('viewcomplaint/', views.viewcomplaint),
    path('viewcomplaint_POST/', views.viewcomplaint_POST),
    path('sendreply/<id>', views.sendreply),
    path('sendreply_POST/', views.sendreply_POST),
    path('Sendbusrelatedmessage_POST/', views.Sendbusrelatedmessage_POST),
    path('Viewbusrelatedmessage_POST/', views.Viewbusrelatedmessage_POST),
    path('viewdrivermessage/', views.viewdrivermessage),
    path('viewdrivermessage_POST/', views.viewdrivermessage_POST),



    path('Logout/', views.Logout),

    path('userlogin_post/', views.userlogin_post),
    path('viewpaymentnotification_POST/', views.viewpaymentnotification_POST),
    path('viewdetectedface_POST/', views.viewdetectedface_POST),
    path('sendcomplaintandviewstatus_POST/', views.sendcomplaintandviewstatus_POST),
    path('viewreply_POST/', views.viewreply_POST),
    path('viewuserprofile_POST/', views.viewuserprofile_POST),
    path('viewdriverprofile_POST/', views.viewdriverprofile_POST),
    path('updatelocation_POST/', views.updatelocation_POST),
    path('viewcheckincheckout_POST/', views.viewcheckincheckout_POST),
    path('viewbusdetails_POST/', views.viewbusdetails_POST),
    path('Sendparentmessage_POST/', views.Sendparentmessage_POST),
    path('Viewparentmessage_POST/', views.Viewparentmessage_POST),
    path('Sendadminmessage_POST/', views.Sendadminmessage_POST),


]

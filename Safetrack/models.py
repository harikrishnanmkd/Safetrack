from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100,default="")
    Password=models.CharField(max_length=100,default="")
    Type=models.CharField(max_length=20,default="")


class Student(models.Model):
    Name=models.CharField(max_length=20,default="")
    Class=models.CharField(max_length=10,default="")
    Housename=models.CharField(max_length=20,default="")
    Division=models.CharField(max_length=20,default="")
    Gender=models.CharField(max_length=10,default="")
    Place=models.CharField(max_length=20,default="")
    Post=models.CharField(max_length=20,default="")
    Pin=models.CharField(max_length=6,default="")
    Guardianname=models.CharField(max_length=20,default="")
    Phonenumber=models.CharField(max_length=10,default="")
    Email=models.CharField(max_length=100,default="")
    Photo=models.CharField(max_length=100,default="")
    Rfidnumber=models.CharField(max_length=100,default="")
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)

class Driver(models.Model):
    Name=models.CharField(max_length=20,default="")
    Housename=models.CharField(max_length=20,default="")
    Place=models.CharField(max_length=20,default="")
    Post=models.CharField(max_length=20,default="")
    Pin=models.CharField(max_length=6,default="")
    Phonenumber=models.CharField(max_length=15,default="")
    Email=models.CharField(max_length=100,default="")
    Experience=models.CharField(max_length=10,default="")
    Photo=models.CharField(max_length=500,default="")
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=2)


class Bus(models.Model):
    Busnumber=models.CharField(max_length=10,default="")
    Registrationnumber=models.CharField(max_length=20)
    Model=models.CharField(max_length=20)
    Driver=models.ForeignKey(Driver,on_delete=models.CASCADE)

class Route(models.Model):
    From_place=models.CharField(max_length=20)
    To_place=models.CharField(max_length=20)
    Amount = models.CharField(max_length=1000)
    Bus=models.ForeignKey(Bus,on_delete=models.CASCADE)

class Allocation(models.Model):
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Bus=models.ForeignKey(Bus,on_delete=models.CASCADE)

class Feepayment(models.Model):
    Student=models.ForeignKey(Student,on_delete=models.CASCADE)
    Date = models.DateField()
    Month=models.CharField(max_length=25)
    Duedate=models.DateField()
    Status=models.CharField(max_length=100)

class Complaint(models.Model):
    complaint=models.CharField(max_length=1000)
    Status=models.CharField(max_length=500)
    Reply=models.CharField(max_length=1000)
    Date=models.DateField()
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Facedetection(models.Model):
    Date = models.DateField()
    Time=models.CharField(max_length=100)
    Photo = models.CharField(max_length=500, default="")
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Busrelatedmessage(models.Model):
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    Message = models.CharField(max_length=500)
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class Location(models.Model):
    Date = models.DateField()
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    Driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class checkincheckout(models.Model):
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    Status = models.CharField(max_length=500)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Parentmessage(models.Model):
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    Message = models.CharField(max_length=500)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

class Drivermessage(models.Model):
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    Message = models.CharField(max_length=500)
    Bus = models.ForeignKey(Bus, on_delete=models.CASCADE)



















from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def login(request):
    return render(request,'loginindex.html')
def login_post(request):
    Username=request.POST['textfield']
    Password=request.POST['textfield2']
    if Login.objects.filter(Password=Password, Username__contains=Username,).exists():
        A=Login.objects.get(Username=Username,Password=Password)
        if A.Password == Password:
            request.session['log']="lin"
            if A.Type=='Admin':
                return  HttpResponse("<script>alert('Login successfully'); window.location='/Safetrack/admin_home/'</script>")
            else:
                return  HttpResponse("<script>alert('User not found'); window.location='/Safetrack/login/'</script>")
        else:
            return HttpResponse("<script>alert('User not found'); window.location='/Safetrack/login/'</script>")

    else:
        return HttpResponse("<script>alert('User not found'); window.location='/Safetrack/login/'</script>")


def admin_home(request):
    return render(request,"admin/indexMain.html")


def Studentregistration(request):
    if request.session['log']=="lin":
       return render(request, 'Admin/Studentregistration.html')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def Studentregistration_post(request):
    if request.session['log'] == "lin":
        Name=request.POST['textfield']
        Class=request.POST['select']
        Division=request.POST['select2']
        Guardianname = request.POST['textfield3']
        Gender=request.POST['gender']
        Housename = request.POST['textfield4']
        Place = request.POST['textfield5']
        Post = request.POST['textfield6']
        Pin = request.POST['textfield7']
        Phonenumber = request.POST['textfield8']
        Email = request.POST['textfield9']
        Photo = request.FILES['file']
        # Password = request.POST['textfield10']
        # ConfirmPassword = request.POST['textfield11']
        from datetime import datetime
        date=datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
        fs=FileSystemStorage()
        fs.save(date,Photo)
        path=fs.url(date)

        B=Login()
        B.Username=Email
        B.Password=Phonenumber
        B.Type='Student'
        B.save()
        res=Student.objects.filter(Email=Email)
        if res.exists():
            return HttpResponse("<script>alert('Already Exist'); window.location='/Safetrack/admin_home/'</script>")

        A=Student()
        A.Name=Name
        A.Class=Class
        A.Division=Division
        A.Guardianname=Guardianname
        A.Gender=Gender
        A.Housename=Housename
        A.Place=Place
        A.Post=Post
        A.Phonenumber=Phonenumber
        A.Email=Email
        A.Photo=path
        A.Pin=Pin
        A.LOGIN_id=B.id
        A.save()
        return HttpResponse('''<script>alert("Registered Succesfully");window.location="/Safetrack/Studentregistration/#about"</script>''')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def Viewstudent(request):
    if request.session['log'] == "lin":
    # search=request.POST["textfield"]
        A=Student.objects.all().order_by('-id')
        l=[]
        for i in A:
            allocated='No'
            if Allocation.objects.filter(Student_id=i.id).exists():
                allocated=str(Allocation.objects.filter(Student_id=i.id)[0].Bus.Busnumber)
            l.append({
                'id':i.id,
                'Name':i.Name,
                'Photo':i.Photo,
                'Class':i.Class,
                'Division':i.Division,
                'Housename':i.Housename,
                'Place':i.Place,
                'Post':i.Post,
                'Pin':i.Pin,
                'Guardianname':i.Guardianname,
                'Phonenumber':i.Phonenumber,
                'Email':i.Email,
                'allocated':allocated,
                'LOGIN': i.LOGIN
                })

        return render(request, 'Admin/Viewstudent.html',{'data':l})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def Viewstudent_post(request):
    if request.session['log'] == "lin":
        search=request.POST["textfield"]
        A=Student.objects.filter(Name__icontains=search) | Student.objects.filter(Class__icontains=search)
        l=[]
        for i in A:
            allocated='No'
            if Allocation.objects.filter(Student_id=i.id).exists():
                allocated=str(Allocation.objects.filter(Student_id=i.id)[0].Bus.Busnumber)
            l.append({
                'id':i.id,
                'Name':i.Name,
                'Photo':i.Photo,
                'Class':i.Class,
                'Division':i.Division,
                'Housename':i.Housename,
                'Guardianname':i.Guardianname,
                'Phonenumber':i.Phonenumber,
                'Email':i.Email,
                'allocated':allocated,
                'LOGIN':i.LOGIN
                })

        return render(request, 'Admin/Viewstudent.html',{'data':l})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editstudent(request,id):
    if request.session['log'] == "lin":
        B=Student.objects.get(LOGIN_id=id)
        return render(request, 'Admin/Editstudent.html',{'data':B})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editstudent_POST(request):
    if request.session['log'] == "lin":
        Name = request.POST['textfield']
        Class = request.POST['select']
        Division = request.POST['select2']
        Guardianname = request.POST['textfield3']
        Gender = request.POST['gender']
        Housename = request.POST['textfield4']
        Place = request.POST['textfield5']
        Post = request.POST['textfield6']
        Pin = request.POST['textfield7']
        Phonenumber = request.POST['textfield8']
        Email = request.POST['textfield9']
        id = request.POST['id']

        A = Student.objects.get(LOGIN_id=id)
        l=Login.objects.filter(id=id).update(Username=Email,Password=Phonenumber)
        if 'file' in request.FILES:
            Photo = request.FILES['file']
            # Password = request.POST['textfield10']
            # ConfirmPassword = request.POST['textfield11']

            from datetime import datetime
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
            fs = FileSystemStorage()
            fs.save(date, Photo)
            path = fs.url(date)
            A.Photo = path
            A.save()
            # A.Name = Name
            # A.Class = Class
            # A.Division = Division
            # A.Guardianname = Guardianname
            # A.Gender = Gender
            # A.Housename = Housename
            # A.Place = Place
            # A.Post = Post
            # A.Phonenumber = Phonenumber
            # A.Email = Email
            # A.Photo = path
            # A.Pin = Pin
            # A.save()

            # l=Login.objects.filter(id=id).update(Username=Email,Password=Phonenumber)
            # return HttpResponse(
            #     '''<script>alert("Registered Succesfully");window.location="/Safetrack/Viewstudent/#about"</script>''')
        # else:
        # A = Student.objects.get(id=id)
        A.Name = Name
        A.Class = Class
        A.Division = Division
        A.Guardianname = Guardianname
        A.Gender = Gender
        A.Housename = Housename
        A.Place = Place
        A.Post = Post
        A.Phonenumber = Phonenumber
        A.Email = Email
        A.Pin = Pin
        A.save()

        return HttpResponse(
            '''<script>alert("Updated Succesfully");window.location="/Safetrack/Viewstudent/#about"</script>''')
    else:
         return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def delete_student(request, id):
        ss = Student.objects.filter(LOGIN_id=id).delete()
        ss = Login.objects.filter(id=id).delete()
        return HttpResponse(
            "<script>alert('Delete Successful'); window.location='/Safetrack/Viewstudent/#about'</script>")


def Driverregistration(request):
    if request.session['log'] == "lin":
        return render(request, 'Admin/Driverregistration.html')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")



def DriverRegistration_Post(request):
    if request.session['log'] == "lin":
        Name=request.POST['textfield']
        Housename = request.POST['textfield2']
        Place = request.POST['textfield3']
        Post = request.POST['textfield4']
        Pin = request.POST['textfield5']
        Phonenumber = request.POST['textfield6']
        Email = request.POST['textfield7']
        Experience = request.POST['select']
        Photo = request.FILES['file']
        # Password = request.POST['textfield9']
        # ConfirmPassword = request.POST['textfield10']

        res = Driver.objects.filter(Email=Email)
        res2 = Driver.objects.filter(Phonenumber=Phonenumber)
        if res.exists() or res2.exists():
            return HttpResponse("<script>alert('Email or Phonenumber Already Exist'); window.location='/Safetrack/admin_home/'</script>")

        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, Photo)
        path = fs.url(date)

        B = Login()
        B.Username = Email
        B.Password = Phonenumber
        B.Type = 'Driver'
        B.save()

        A=Driver()
        A.Name=Name
        A.Housename=Housename
        A.Place=Place
        A.Post=Post
        A.Pin=Pin
        A.Phonenumber=Phonenumber
        A.Email=Email
        A.Experience=Experience
        A.Photo=path
        A.LOGIN_id=B.id
        A.save()
        return HttpResponse('''<script>alert("Registered Succesfully");window.location="/Safetrack/Driverregistration/#about"</script>''')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")



def Viewdriver(request):
    if request.session['log'] == "lin":
        A=Driver.objects.all().order_by('-id')
        return render(request, 'Admin/Viewdriver.html',{'data':A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def delete_driver(request, id):
        ss = Driver.objects.filter(id=id).delete()
        return HttpResponse(
            "<script>alert('Delete Successful'); window.location='/Safetrack/Viewdriver/#about'</script>")


def Editdriver(request,id):
    if request.session['log'] == "lin":
        B = Driver.objects.get(LOGIN_id=id)
        return render(request, 'Admin/Editdriver.html',{'data':B})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def Editdriver_POST(request):
    if request.session['log'] == "lin":
        Name=request.POST['textfield']
        Housename = request.POST['textfield2']
        Place = request.POST['textfield3']
        Post = request.POST['textfield4']
        Pin = request.POST['textfield5']
        Phonenumber = request.POST['textfield6']
        Email = request.POST['textfield7']
        Experience = request.POST['select']

        id=request.POST['id']
        # Password = request.POST['textfield9']
        # ConfirmPassword = request.POST['textfield10']

        A=Driver.objects.get(LOGIN_id=id)
        if 'file' in request.FILES:
            Photo = request.FILES['file']
            if Photo !="":
                from datetime import datetime
                date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
                fs = FileSystemStorage()
                fs.save(date, Photo)
                path = fs.url(date)
                A.Photo = path
                A.save()

        A.Name=Name
        A.Housename=Housename
        A.Place=Place
        A.Post=Post
        A.Pin=Pin
        A.Phonenumber=Phonenumber
        A.Email=Email
        A.Experience=Experience
        A.save()
        l = Login.objects.filter(id=id).update(Username=Email, Password=Phonenumber)
        return HttpResponse('''<script>alert("Updated Succesfully");window.location="/Safetrack/Viewdriver/#about"</script>''')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")




def Searchdriver(request):
    if request.session['log'] == "lin":
        search = request.POST["textfield"]
        A = Driver.objects.filter(Name__icontains=search)
        return render(request, 'Admin/Viewdriver.html',{'data':A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")




def Busregistration(request):
    if request.session['log'] == "lin":
        A = Driver.objects.all()
        return render(request, 'Admin/Busregistration.html',{"data":A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Busregistration_Post(request):
    if request.session['log'] == "lin":
        Busnumber=request.POST['textfield']
        Registrationnumber = request.POST['textfield2']
        Model = request.POST['textfield3']
        Driver = request.POST['select']
        d=Bus.objects.filter(Busnumber=Busnumber)
        l=Bus.objects.filter(Driver__id=Driver)
        m=Bus.objects.filter(Registrationnumber=Registrationnumber)

        if d.exists():
            return HttpResponse("<script>alert('Choose another Busnumber'); window.location='/Safetrack/Busregistration/#about'</script>")

        if l.exists():
            return HttpResponse("<script>alert('Choose another Driver'); window.location='/Safetrack/Busregistration/#about'</script>")
        if m.exists():
            return HttpResponse("<script>alert('Choose another Driver'); window.location='/Safetrack/Busregistration/#about'</script>")

        else:
            A=Bus()
            A.Busnumber=Busnumber
            A.Registrationnumber=Registrationnumber
            A.Model=Model
            A.Driver_id=Driver
            A.save()
            return HttpResponse('''<script>alert("Registered Succesfully");window.location="/Safetrack/Busregistration/#about"</script>''')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def Viewbus(request):
        if request.session['log'] == "lin":
            A = Bus.objects.all().order_by('-id')
            l=[]
            for i in A:
                if Location.objects.filter(Driver_id=i.Driver.id).exists():
                    print(i.Driver.id)
                    r=Location.objects.get(Driver_id=i.Driver.id)
                    print(r.Latitude)

                    l.append({"id":i.id,"Busnumber":i.Busnumber,"Registrationnumber":i.Registrationnumber,"Model":i.Model,"Dname":i.Driver.Name,"Latitude":r.Latitude,"Longitude":r.Longitude})
                else:
                    l.append({"id":i.id,"Busnumber":i.Busnumber,"Registrationnumber":i.Registrationnumber,"Model":i.Model,"Dname":i.Driver.Name,"Latitude":""})

            return render(request, 'Admin/Viewbus.html', {'data': l})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Viewbus_POST(request):
    if request.session['log'] == "lin":
        search=request.POST["textfield"]
        A=Bus.objects.filter(Busnumber__icontains=search)
        return render(request, 'Admin/Viewbus.html',{'data':A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editbus(request,id):
    if request.session['log'] == "lin":
        A = Driver.objects.exclude(id__in=Bus.objects.all().values_list('Driver_id'))
        B=Bus.objects.get(id=id)
        return render(request, 'Admin/Editbus.html',{"data":A,"data1":B})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editbus_POST(request):
    if request.session['log'] == "lin":
        Bid=request.POST['id']
        Busnumber=request.POST['textfield']
        Registrationnumber = request.POST['textfield2']
        Model = request.POST['textfield3']
        Driver = request.POST['select']


        A=Bus.objects.get(id=Bid)
        A.Busnumber=Busnumber
        A.Registrationnumber=Registrationnumber
        A.Model=Model
        A.Driver_id=Driver
        A.save()
        return HttpResponse('''<script>alert("Registered Succesfully");window.location="/Safetrack/Viewbus/#about"</script>''')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def delete_bus(request,id):
    ss=Bus.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete Successful'); window.location='/Safetrack/Viewbus/#about'</script>")

def Addroute(request):
    if request.session['log'] == "lin":
        A = Bus.objects.all()
        return render(request, 'Admin/Addroute.html',{"data":A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Addroute_POST(request):
        if request.session['log'] == "lin":
            Fromplace = request.POST['textfield']
            ToPlace = request.POST['textfield2']
            Amount = request.POST['textfield3']
            bus = request.POST['select']
            c=Route.objects.filter(Bus_id=bus)
            if c.exists():
                return HttpResponse(
                    '''<script>alert("Choose another Bus");window.location="/Safetrack/Addroute/#about"</script>''')
            else:
                A = Route()
                A.From_place= Fromplace
                A.To_place = ToPlace
                A.Amount = Amount
                A.Bus_id = bus
                A.save()
                return HttpResponse(
                    '''<script>alert("Registered Succesfully");window.location="/Safetrack/Addroute/#about"</script>''')
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def ViewRoute(request):
        if request.session['log'] == "lin":
            A = Route.objects.all().order_by('-id')
            return render(request, 'Admin/ViewRoute.html', {'data': A})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def ViewRoute_post(request):
    if request.session['log'] == "lin":
        search=request.POST["textfield"]
        A=Route.objects.filter(Bus__Busnumber__icontains=search)
        return render(request, 'Admin/Viewroute.html',{'data':A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editroute(request, id):
        if request.session['log'] == "lin":
            A = Bus.objects.all()
            B = Route.objects.get(id=id)
            return render(request, 'Admin/Editroute.html', {"data": A, "data1": B})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editroute_POST(request):
        if request.session['log'] == "lin":
            id=request.POST['id']
            Fromplace = request.POST['textfield']
            ToPlace = request.POST['textfield2']
            Amount = request.POST['textfield3']
            bus = request.POST['select']

            if Route.objects.filter(Bus_id = bus).exists():
                return HttpResponse('''<script>alert("Already Allocated");window.location="/Safetrack/Viewroute/#about"</script>''')

            A = Route.objects.get(id=id)
            A.From_place = Fromplace
            A.To_place = ToPlace
            A.Amount = Amount
            A.Bus_id = bus
            A.save()
            return HttpResponse(
                '''<script>alert("Updated Succesfully");window.location="/Safetrack/Viewroute/#about"</script>''')
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def delete_route(request,id):
    ss=Route.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete Successful'); window.location='/Safetrack/Viewroute/#about'</script>")


def Allocationsb(request,id):
    if request.session['log'] == "lin":
        A = Bus.objects.all()
        # b=Student.objects.all()
        return render(request, 'Admin/Allocation.html',{"data":A,'data1':id})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Allocation_POST(request):
        if request.session['log'] == "lin":
            bus = request.POST['select1']
            student = request.POST['select']

            A = Allocation()
            A.Bus_id = bus
            A.Student_id=student
            A.save()
            return HttpResponse(
                '''<script>alert("Registered Succesfully");window.location="/Safetrack/Viewstudent/"</script>''')
        else:

            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Viewallocation(request):
        if request.session['log'] == "lin":
            A = Allocation.objects.all().order_by('-id')
            return render(request, 'Admin/Viewallocation.html', {'data': A})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Viewallocation_post(request):
    if request.session['log'] == "lin":
        search=request.POST["textfield"]
        A=Allocation.objects.filter(Bus__Busnumber__icontains=search)
        return render(request, 'Admin/Viewallocation.html',{'data':A})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editallocation(request, id):
    if request.session['log'] == "lin":
        A = Bus.objects.all()
        b = Student.objects.all()
        d=Allocation.objects.get(id=id)
        return render(request, 'Admin/Editallocation.html', {"data": A, 'data1': b,'data3':d})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def Editallocation_POST(request):
        if request.session['log'] == "lin":
            id = request.POST['id']
            bus = request.POST['select1']
            # student = request.POST['select']

            A = Allocation.objects.get(id=id)
            A.Bus_id = bus
            # A.Student_id = student
            A.save()
            return HttpResponse(
                '''<script>alert("Registered Succesfully");window.location="/Safetrack/Viewallocation/#about"</script>''')
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def delete_allocation(request,id):
    ss=Allocation.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete Successful'); window.location='/Safetrack/Viewallocation/#about'</script>")


def sendpaymentnotification(request):
    if request.session['log'] == "lin":
        return render(request, 'Admin/paymentnotification.html')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def sendpaymentnotification_POST(request):
    if request.session['log'] == "lin":
        Duedate = request.POST['textfield']
        Month = request.POST['select']

        c=Student.objects.filter()
        for i in c:
            d=Feepayment()
            d.Student=i
            import datetime
            d.Date=datetime.date.today()
            d.Duedate=Duedate
            d.Month=Month
            d.Status='pending'
            d.save()


        return HttpResponse(
            '''<script>alert("Registered Succesfully");window.location="/Safetrack/sendpaymentnotification/#about"</script>''')
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def viewpaymentnotification(request):
        if request.session['log'] == "lin":
            a = Feepayment.objects.all()
            return render(request, 'Admin/viewpaymentnotification.html', {'data': a})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def viewpaymentnotification_post(request):
    if request.session['log'] == "lin":
        a=Feepayment.objects.all()
        return render(request, 'Admin/viewpaymentnotification.html',{'data':a})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def delete_paymentnotification(request,id):
    ss=Feepayment.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Delete Successful'); window.location='/Safetrack/viewpaymentnotification/#about'</script>")

def viewcomplaint(request):
        if request.session['log'] == "lin":
            a = Complaint.objects.filter().order_by('-id')
            return render(request, 'Admin/viewcomplaints.html', {'data': a})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def viewcomplaint_POST(request):
    if request.session['log'] == "lin":
        Fromdate=request.POST['textfield1']
        Todate=request.POST['textfield2']
        a=Complaint.objects.filter(Date__range=[Fromdate,Todate]).order_by('-id')
        return render(request, 'Admin/viewcomplaints.html',{'data':a})
    else:
         return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def sendreply(request,id):
    if request.session['log'] == "lin":
        return render(request, 'Admin/sendreply.html',{'id':id})
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")

def sendreply_POST(request):
    if request.session['log'] == "lin":
        Reply=request.POST["textfield"]
        id=request.POST['id']
        Complaint.objects.filter(id=id).update(Reply=Reply,Status='Replied')
        return HttpResponse("<script>alert('Replayed'); window.location='/Safetrack/viewcomplaint/'</script>")
    else:
        return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def viewdrivermessage(request):
        if request.session['log'] == "lin":
            A = Drivermessage.objects.all().order_by('-id')
            return render(request, 'Admin/viewmessage.html', {'data': A})
        else:
            return HttpResponse("<script>alert('Your Loged Out'); window.location='/Safetrack/login/'</script>")


def viewdrivermessage_POST(request):
    a=Drivermessage.objects.filter()
    return render(request, 'Admin/viewmessage.html', {'data': a})


def Logout(request):
    request.session['log']=""
    return render(request, 'loginindex.html')



                   #####################################################################################################



def userlogin_post(request):
    Username=request.POST['name']
    Password=request.POST['password']
    res=Login.objects.filter(Username=Username,Password=Password)
    if res.exists():
        ress = Login.objects.get(Username=Username, Password=Password)
        if ress.Type=="Student":
            ss=Student.objects.get(LOGIN__id=ress.id)
            return JsonResponse({"status":"ok","lid":str(ress.id),"type":ress.Type,"uname":ss.Name,"uemail":ss.Email,"uphoto":ss.Photo})
        if ress.Type=="Driver":
                    ss=Driver.objects.get(LOGIN__id=ress.id)
                    return JsonResponse({"status":"ok","lid":str(ress.id),"type":ress.Type,"uname":ss.Name,"uemail":ss.Email,"uphoto":ss.Photo})
        else:
            return JsonResponse({"status":"none"})
    else:
        return JsonResponse({"status": "ok"})




def viewpaymentnotification_POST(request):
    Lid=request.POST['lid']
    res=Feepayment.objects.filter(Student__LOGIN=Lid)
    l=[]
    for i in res:
        a=Allocation.objects.filter(Student__LOGIN_id=Lid)
        amt = '0'
        if a.exists():
            amt=Route.objects.filter(Bus=a[0].Bus)[0].Amount
        l.append({'id':i.id,'Student':i.Student.Name,'Date':i.Date,'Duedate':i.Duedate,'Month':i.Month,'Amount':amt})
    return JsonResponse({"status": "ok",'data':l})


def sendcomplaintandviewstatus_POST(request):
    Lid=request.POST['lid']
    complaint=request.POST['complaint']
    # Status=['Pending']
    # Reply=['Pending']
    c=Complaint()
    c.complaint=complaint
    c.Status='Pending'
    c.Reply='Pending'
    from datetime import datetime
    c.Date=datetime.now().today()
    c.Student=Student.objects.get(LOGIN=Lid)
    c.save()
    return JsonResponse({"status": "ok"})

# def studentviewprofile_POST(request):

def viewdetectedface_POST(request):
    Lid = request.POST['lid']
    a=Facedetection.objects.filter(Student__LOGIN_id=Lid).order_by('-id')
    l = []
    for i in a:
        l.append({'id':i.id,'Student':i.Student.Name,'Date':i.Date,'Time':i.Time,'Photo':i.Photo})
    return JsonResponse({"status": "ok",'data':l})



def viewreply_POST(request):
    Lid = request.POST['lid']
    a=Complaint.objects.filter(Student__LOGIN_id=Lid).order_by('-Date')
    l=[]
    for i in a:
        l.append({'id':i.id,'complaint':i.complaint,'Status':i.Status,'Reply':i.Reply,'Date':i.Date})
    return JsonResponse({"status": "ok",'data':l})


def viewuserprofile_POST(request):
    Lid = request.POST['lid']
    print(Lid)
    a=Student.objects.get(LOGIN_id=Lid)
    return JsonResponse({"status": "ok",'Name':a.Name,'Class':a.Class,'Division':a.Division,'Photo':a.Photo,'Email':a.Email})

def makefeepayment_POST(request):
    Fid = request.POST['fid']
    a=Feepayment.objects.filter(id=Fid).update(Status='paid')
    return JsonResponse({"status": "ok"})


def viewdriverprofile_POST(request):
    Lid = request.POST['lid']
    print(Lid)
    a=Driver.objects.get(LOGIN_id=Lid)
    return JsonResponse({"status": "ok",'Name':a.Name,'Photo':a.Photo,'Email':a.Email})

def Sendbusrelatedmessage_POST(request):
    Lid = request.POST['lid']
    Message = request.POST['Message']
    a=Busrelatedmessage()
    a.Driver=Driver.objects.get(LOGIN_id=Lid)
    a.Message=Message
    from datetime import datetime
    a.Date=datetime.now().date()
    a.Time=datetime.now().time()
    a.save()


    return JsonResponse({"status":"ok"})

def Viewbusrelatedmessage_POST(request):
    Lid=request.POST['lid']
    bb=Allocation.objects.get(Student__LOGIN_id=Lid).Bus.Driver.id
    a = Busrelatedmessage.objects.filter(Driver=bb).order_by('-Date','-Time')
    l = []
    for i in a:
        l.append({'id': i.id, 'Driver': i.Driver.Name, 'Date': i.Date, 'Time': i.Time,'Message':i.Message})
    return JsonResponse({"status": "ok", 'data': l})


def updatelocation_POST(request):


    Lid = request.POST['lid']

    Latitude = request.POST['Latitude']
    Longitude = request.POST['Longitude']

    a=Driver.objects.get(LOGIN_id=Lid)
    print(a)

    if Location.objects.filter(Driver_id=a.id).exists():
        b = Location.objects.get(Driver_id=a.id)
        b.Driver = a
        b.Latitude = Latitude
        b.Longitude = Longitude
        from datetime import datetime
        b.Date = datetime.now().date()
        b.save()
        return JsonResponse({"status": "ok"})
    else:
        b=Location()
        b.Driver=a
        b.Latitude=Latitude
        b.Longitude=Longitude
        from datetime import datetime
        b.Date=datetime.now().date()
        b.save()

        return JsonResponse({"status": "ok"})

def viewcheckincheckout_POST(request):
    Lid = request.POST['lid']
    a=checkincheckout.objects.filter(Student__LOGIN_id=Lid).order_by('-Date')
    l=[]
    for i in a:
        l.append({'id':i.id,'Status':i.Status,'Time':i.Time,'Date':i.Date})
    return JsonResponse({"status": "ok",'data':l})


def viewbusdetails_POST(request):
    Lid = request.POST['lid']
    print(Lid)
    std = Student.objects.get(LOGIN_id=Lid)
    print(std)
    alls = Allocation.objects.get(Student__LOGIN_id=Lid).Bus.Driver.id
    print(alls)
    bb = Location.objects.filter(Driver_id=alls)
    l = []
    print(bb)
    for i in bb:
        b = Bus.objects.filter(Driver=i.Driver)
        l.append({'id':b[0].id,
                  'Busnumber':b[0].Busnumber,
                  'Name':i.Driver.Name,
                  'Phonenumber':i.Driver.Phonenumber,
                  'Email':i.Driver.Email,
                  'Latitude':i.Latitude,
                  'Longitude':i.Longitude,
                  })
    return JsonResponse({"status": "ok",'data':l})



def Sendparentmessage_POST(request):
    Lid = request.POST['lid']
    Did = request.POST['Did']
    Message = request.POST['Message']
    a=Parentmessage()
    a.Bus_id=Did
    a.Student=Student.objects.get(LOGIN_id=Lid)
    a.Message=Message
    from datetime import datetime
    a.Date=datetime.now().date()
    a.Time=datetime.now().time()
    a.save()
    return JsonResponse({"status": "ok"})

def Viewparentmessage_POST(request):
    Lid=request.POST['lid']
    # bb=B.objects.get(Student__LOGIN_id=Lid).Bus.Driver.id
    a = Parentmessage.objects.filter(Bus__Driver__LOGIN__id=Lid).order_by('-Date','-Time')
    l = []
    for i in a:
        l.append({'id': i.id, 'Student': i.Student.Name, 'Date': i.Date, 'Time': i.Time,'Message':i.Message})
    return JsonResponse({"status": "ok", 'data': l})


def Sendadminmessage_POST(request):
    Lid = request.POST['lid']
    Message = request.POST['Message']
    a=Drivermessage()
    a.Bus=Bus.objects.get(Driver__LOGIN_id=Lid)
    a.Message=Message
    from datetime import datetime
    a.Date=datetime.now().date()
    a.Time=datetime.now().time()
    a.save()
    return JsonResponse({"status": "ok"})
















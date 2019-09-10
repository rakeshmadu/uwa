from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
from .models import Admin,User,Booking
from .forms import AdminRegister,Login,TicketBooking,userLogin,UserRegister
from django.core.mail import send_mail
from random import randint
from django.db.models import Sum

# Create your views here.
def Home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'admin.html')
def userreg(request):
    return render(request,'admin.html')
def UserHome(request):
    return render(request,'userhome.html')

def adminRegister(request):
    form=AdminRegister()
    if request.method=='POST':
        form=AdminRegister(request.POST)
        if form.is_valid():
            # n='KV'
            # for i in range(0,4):
            #     n=n+str(randint(0,9))
            # reg_id=n
            name=form.cleaned_data['name']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            mobileno=form.cleaned_data['mobileno']
            k=Admin(username=username,name=name,password=password,email=email,mobileno=mobileno)
            k.save() 
            if not k:
                return HttpResponse("Registration not completed")
            else:
                return redirect("/adminlog")
            # reg_id=request.session['id']=k.reg_id
            # sub="registration success"
            # sender='kavipy2@gmail.com'
            # msg="Hello Mr/Ms."+request.POST['name']+"\n"+"register_id:"+reg_id+"\n"+"\n""Password:"+request.POST['password']+"\n"+"your application submited successfully."+"\n"+"- It is auto genrated yahoo mail."
            # # msg2="Thank you for register"+"\n"+"it is auto generated mail"
            # to=request.POST['email']
            # send_mail(sub,msg,sender,[to]) 
    return render(request,'register.html',{'form':form})
def adminLogin(request):
    form=Login()
    if request.method=='POST':
        form=Login(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name'] 
            request.session['name']=name
            password =form.cleaned_data['password']
            user=Admin.objects.filter(name=name,password=password)
            if not user:
                return HttpResponse("""login failed""")
            else:
                return redirect("/userhome")
    return render(request,'ulogin.html',{'form':form})
def bookings(request):
    form=TicketBooking()
    if request.method=='POST':
        form=TicketBooking(request.POST)
        if form.is_valid():
            n=''
            for i in range(0,4):
                n=n+str(randint(0,9))
            reg_id=n
            name=form.cleaned_data['name']
            # password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            mobile=form.cleaned_data['mobile']
            age=form.cleaned_data['age']
            parks_names=form.cleaned_data['parks_names']
            # cost=form.cleaned_data['cost']
            # totaltickets=form.cleaned_data['totaltickets']
            child=form.cleaned_data['child']
            c=50*int(child)
            adult=form.cleaned_data['adult']
            a=100*int(adult)
            cost=c+a
            total=int(child)+int(adult)
            print(cost)
            country=form.cleaned_data['country']
            status=form.cleaned_data['status']
            state=form.cleaned_data['state']
            date=form.cleaned_data['date']
            city=form.cleaned_data['city']
            idproof=form.cleaned_data['idproof']
            idno=form.cleaned_data['idno']
            vehicle_no=form.cleaned_data['vehicle_no']  
            # reg_id=form.cleaned_data['reg_id']
            k=Booking(reg_id=reg_id,name=name,email=email,status=status,mobile=mobile,age=age,parks_names=parks_names,cost=cost,total=total,adult=adult,child=child,country=country,state=state,date=date,city=city,idproof=idproof,idno=idno,vehicle_no=vehicle_no)
            k.save()
            reg_id=request.session['id']=k.reg_id
            sub="registration success"
            sender='kavipy2@gmail.com'
            msg="Hello Mr/Ms."+request.POST['name']+"\n"+"register_id:"+reg_id+"\n"+"date:"+request.POST['date']+"\n"+"cost:"+str(cost)+"\n"+"your ticket is booked  successfully."+"\n"+"-It is auto genrated  gmail."
            # msg2="Thank you for register"+"\n"+"it is auto generated mail"
            to=request.POST['email']
            send_mail(sub,msg,sender,[to])
            return render(request,'ticket.html',{'form':form,'status':status,'parks_names':parks_names,'total':total,'ticket_id':k.reg_id,'cost':cost,'adult':adult,'parks_names':parks_names,'child':child,'Date':date})

    return render(request,'booking.html',{'form':form})    

def getdtls(request):
    # if request.method=='POST':
    name1=request.session['name']
    # print(name1)
    dbuser=Booking.objects.filter(name=name1)
    if dbuser:
        return render(request,'display.html',{'name':dbuser})
    else:
        return HttpResponse("previously  no bookings  ..... please Book A Ticket...")

    # dtls=Booking.objects.all()
    # return render(request,'display.html',{'dtls':dtls})
    # return render(request,'display.html')

def alldetails(request):
    all=Booking.objects.all()
    # all.save()
    return render(request,'details.html',{'all':all})


def pflow(request):
    ice  =  Booking.objects.filter(country='Iceland').count()
    ind  =  Booking.objects.filter(country='India').count()
    ud   =  Booking.objects.filter(country='Uganda').count()
    tk   =  Booking.objects.filter(country='Turkey').count()
    a    =  Booking.objects.filter(country='Austria').count()
    bn   =  Booking.objects.filter(country='Bangladesh').count()
    bl   =  Booking.objects.filter(country='Belize').count()
    ca   =  Booking.objects.filter(country='Canada').count() 
    xdata1 = ["Iceland","India","Uganda","Turkey","Austria","Bangladesh","Belize","Canada"]
    ydata1 = [ice,ind,ud,tk,a,bn,bl,ca]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata1, 'y1': ydata1, 'extra1': extra_serie}
    charttype = "discreteBarChart"
    u  = Booking.objects.filter(parks_names='Queen Elizabeth national park').count()
    m  = Booking.objects.filter(parks_names='Murchison falls national park').count()
    b  = Booking.objects.filter(parks_names='Bwindi impenetrable national park').count()
    l  = Booking.objects.filter(parks_names='Lake Mburo national Park').count()
    k  = Booking.objects.filter(parks_names='Kidepo Valley National Park').count()
    s  = Booking.objects.filter(parks_names='Semuliki National Park').count()
    e  = Booking.objects.filter(parks_names='Mt Elgon National Park').count()
    g  = Booking.objects.filter(parks_names='Mgahinga Gorilla National Park').count()
    xdata2 = ["Queen Elizabeth","Murchison","Lake Mburo","Bwindi","Kidepo Valley","Semuliki","Mt Elgon","Mgahinga"]
    ydata2 = [u,m,b,l,k,s,e,g]

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata2   = {'x': xdata2, 'y1': ydata2, 'extra2': extra_serie1}
    charttype2   = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,

        'chartdata2':chartdata2,
        'charttype2':charttype2,
        'extra2': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,

            'chart_attr': {

                'labelType': '\"percent\"',
            }
        }

    }
    return render_to_response('pflow.html', data)

def multp(request):
    add= Booking.objects.all().aggregate(Sum('total'))
    adding=Booking.objects.all().aggregate(Sum('cost'))
    return render(request,'sales.html',{'add':add['total__sum'],"adding":adding['cost__sum']})

def invid(request,id):
    tic = Booking.objects.get(id=id)
    return render(request,"invid.html",{'form':tic})
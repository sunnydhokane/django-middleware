from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,Addproblem,Addtopic
from django.contrib import messages
from .models import Problem, Sources
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,'index.html')

def register(request):
    form_pre = UserForm()
    if request.method == 'POST':
        form_pre = UserForm(request.POST)
        if form_pre.is_valid():
            form_pre.save()
            messages.success(request, 'Account created successfully..')
            return redirect('login')
    context = {'form': form_pre}
    return render(request,"register.html",context)

#--Login view-->
def loginuser(request):
    if request.method == 'POST':

        username_entered = request.POST.get('username')
        password_entered = request.POST.get('password')

        user = authenticate(request,username = username_entered, password = password_entered)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"username or password is incorrect...")
    context = {}
    return render(request,"login.html",context)

@login_required(login_url='login')
def problems(request):
    mydata = Problem.objects.all().values()
    mydata1=Problem.objects.values('topic').distinct()
    print(mydata1)
    data={
        'mydata':mydata,
        'mydata1':mydata1
    }
    return render(request,"problem.html",data)

def logoutuser(request):
    logout(request)
    return redirect('register')

@login_required(login_url='login')
def topics(request):
    mydata=Sources.objects.all().values()
    mydata1 = Sources.objects.values('topic').distinct()
    data={
        'mydata':mydata,
        'mydata1':mydata1
    }
    return render(request,"topics.html",data)

@login_required(login_url='login')
def discuss(request):
    return redirect('https://chat-ez2x.onrender.com/')

def pfilter(request):
    mydata = Problem.objects.all().values()
    mydata1 = Problem.objects.values('topic').distinct()
    k=1
    d = []
    if(request.method == 'POST'):
        res_rate=request.POST.get("Rate",None)
        print(res_rate)
        if(res_rate==None):
            k=0
        for i in mydata:
            print(i)
            if(i['topic']==res_rate):
                d.append(i)
    if(k==1):
        data = {
            'mydata': d,
            'mydata1': mydata1
        }
        return render(request,"problem.html",data)
    data = {
        'mydata': mydata,
        'mydata1': mydata1
    }
    return render(request,"problem.html",data)

def tfilter(request):
    mydata = Sources.objects.all().values()
    mydata1 = Sources.objects.values('topic').distinct()
    k=1
    d = []
    if(request.method == 'POST'):
        res_rate=request.POST.get("Rate",None)
        print(res_rate)
        if(res_rate==None):
            k=0
        for i in mydata:
            print(i)
            if(i['topic']==res_rate):
                d.append(i)
    if(k==1):
        data = {
            'mydata': d,
            'mydata1': mydata1
        }
        return render(request,"topics.html",data)
    data = {
        'mydata': mydata,
        'mydata1': mydata1
    }
    return render(request,"topics.html",data)

@login_required(login_url='login')
def AddProblem(request):
    form_pre = Addproblem()
    if request.method == 'POST':
        form_pre = Addproblem(request.POST)
        if form_pre.is_valid():
            Problem.objects.create(**form_pre.cleaned_data)
            return redirect('problems')
        else:
            return redirect('problems')
    context = {'form': form_pre}
    return render(request, "AddProblem.html", context)

@login_required(login_url='login')
def AddTopic(request):
    form_pre = Addtopic()
    if request.method == 'POST':
        form_pre = Addtopic(request.POST)
        if form_pre.is_valid():
            Sources.objects.create(**form_pre.cleaned_data)
            return redirect('topics')
        else:
            return redirect('topics')
    context = {'form': form_pre}
    return render(request, "AddTopic.html", context)




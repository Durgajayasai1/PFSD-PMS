from django.shortcuts import render
from .forms import UserForm
from .models import User_Details
# Create your views here.
def home(r):
    return render(r,'home.html',{})
def login1(request):
    x=request.POST.get("username")
    y=request.POST.get("password")
    z=User_Details.objects.filter(username=x,password=y)
    print(z)
    if z:
        return render(request,'inhome.html',{'x':id})
    else:
        return render(request,'login.html',{'mess':'Credentials Wrong'})
def signup1(request):
    if request.method=='POST':
        x=UserForm(request.POST or None)
        print(x)
        if x.is_valid:
            x.save()
            return render(request,'login.html')
        else:
            return render(request,'signup.html')
def signup(request):
     return render(request,'signup.html')
def login(y):
    return render(y, 'login.html',{})
def project(p):
    return render(p, 'project.html',{})
def sidebar(sb):
    return render(sb, 'sidebar.html',{})
def todo(t):
    return render(t, 'todo.html',{})
def inhome(h):
    return render(h, 'inhome.html', {})
def contactus(c):
    return render(c, 'contactus.html', {})
def profile(pro):
    return render(pro, 'profile.html', {})
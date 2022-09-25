from django.shortcuts import render,redirect
from ada.models import userdetail
# Create your views here.
def index(request):
    request.session['usr']=""
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        if userdetail.objects.filter(email=request.POST['your-email']).exists():
            return redirect('ada:signup')
        else:
            userdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
            return redirect('ada:login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        if (request.POST['inputEmail']=='admin@gmail.com' and request.POST['inputPassword']=='@1geniUs'):
            print('YSE')
            request.session['usr']='admin'
            return redirect('ada:admindash')
        elif userdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():

            request.session['usr']=request.POST['inputEmail']
            return redirect('ada:dashboard')
        else:
            print('NO')
            return redirect('ada:login')
    return render(request,'login.html')

def logout(request):
    request.session['usr']=""
    return render(request,'index.html')

def dashboard(request):
    if request.session['usr']:
        return render(request,'dashboard.html')
    else:
        return redirect('ada:login')

def admindash(request):
    if (request.session['usr'] and request.session['usr']=='admin'):
        return render(request,'admin.html')
    else:
        return redirect('ada:login')

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,User

# Create your views here.
def Homepage(request):
    return HttpResponse("<h1>Welcome to My Site</h1>")

def products(request):
    cards = Product.objects.all()
    return render(request,'index.html',{'cards':cards})

def register(request):
    email = request.GET.get('email')
    password = request.GET.get('password')
    mobile = request.GET.get('mobile')
    fullname = request.GET.get('fullname')

    if email and password:
        newinput = User.objects.create(email=email, password=password,mobile=mobile, fullname=fullname)
        print(newinput)
        newinput.save()
    data = User.objects.all()
    return render(request,'register.html',{'data':data})

def login(request):
    email = request.GET.get('email')
    password = request.GET.get('password')

    if email and password:
        try:
            user = User.objects.get(email=email, password=password)
            print(user)
            return HttpResponse("<h1>Welcome {user.email}</h1>")
        except User.DoesNotExist:
            return HttpResponse("<h1>Invalid credentials</h1>")
    return render(request, 'login.html')

def checkout(request):
    return render(request, 'cart.html')
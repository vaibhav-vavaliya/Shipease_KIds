from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product,Cart
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate

# Create your views here.
def Homepage(request):
    # print(request.user.id)
    return render(request, 'home.html')
def products(request):
    cards = Product.objects.all()
    return render(request,'index.html',{'cards':cards})

def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    mobile = request.POST.get('mobile')
    fullname = request.POST.get('fullname')

    # Check if email is not exist before creating a new user
    if User.objects.filter(email=email).exists():
        return HttpResponse("<h1>Email already exists</h1>")

    if email and password:
        newinput = User.objects.create_user(email=email, password=password, username=fullname)
        # print(newinput)
        newinput.save()
    data = User.objects.all()
    return render(request,'register.html',{'data':data})

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # print(username, password)

    if username and password:
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # print(user)
            auth.login(request, user)
            return redirect('/')
        else:
            return HttpResponse("<h1>Invalid credentials</h1>")
    return render(request, 'login.html')

def cart(request):
    uid = request.GET.get('uid')
    uid = request.user.id
    values = Cart.objects.filter(user_id=uid)
    # print(uid)
    return render(request, 'cart.html', {"values": values})
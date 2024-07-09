from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from django.contrib import messages

# Create your views here.
def urlpass(request,d):
    print(type(d))
    f=8
    if d%2==0:
        return HttpResponse("%s is Even no %s"%(d,f))
    else:
        return HttpResponse("%s is Odd no"%d)

def home(request):
    if request.method=='POST':
        a=int(request.POST['n1'])
        print(type(a))
        return render(request,'home.html',{'data':a})   #context method
    return render(request,'home.html')
def ind(request):
    l=['apple','orange',56,78]
    d={1:'anu',2:'appu',3:'azrin'}
    d1=[{1:'anu',2:'appu',3:'azrin'}]
    return render(request,'ind.html',{'l':l,'d':d,'d1':d1})


def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['phno']
        c=request.POST['email']
        d=request.POST['username']
        e=request.POST['password']
        f=request.POST['confirm_password']
        if user_register.objects.filter(username=d).exists():
            messages.error(request,'Username Already Exists')
        else:
            if e==f:
                data=user_register(name=a,email=c,phno=b,username=d,password=e)
                data.save()
                messages.success(request,'Registered successfully')
            else:
                messages.error(request,'Password Does not Match')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        d = request.POST['username']
        e = request.POST['password']
        try:
            data=user_register.objects.get(username=d)
            if data.password==e:
                request.session['user']=d
                return redirect(userhome)
            else:
                messages.error(request,'incorrect password')
        except:
            if d=='admin' and e=='admin':
                request.session['admin']=d
                return redirect(adminhome)
            messages.error(request,"incorrect username")
    return render(request,'login.html')


def userhome(request):
    if 'user'  in request.session:
        data=product.objects.all()
        return render(request,'userhome.html',{'data':data})
    return redirect(login)

def adminhome(request):
    if 'admin' in request.session:
        return render(request,'adminhome.html')
    return redirect(login)

def add_product(request):
    if 'admin' in request.session:
        if request.method=='POST':
            a = request.POST['name']
            b = request.POST['price']
            c = request.POST['stock']
            d = request.FILES['img']
            product.objects.create(cake_name=a,cake_price=b,cake_stock=c,cake_img=d).save()
            messages.success(request,'Cake added successfully')
            return redirect(add_product)
        return render(request,'add_product.html')
    return redirect(login)


def manage_product(request):
    if 'admin' in request.session:
        data=product.objects.all()
        return render(request,'manage_product.html',{'data':data})
    return redirect(login)

def update_product(request,d):
    if 'admin' in request.session:
        data=product.objects.get(pk=d)
        if request.method=='POST':
            a = request.POST['name']
            b = request.POST['price']
            c = request.POST['stock']
            # d = request.FILES['img']
            product.objects.filter(pk=d).update(cake_name=a,cake_price=b,cake_stock=c)
            messages.success(request,"cake updated sucessfully")
            return redirect(manage_product)
        return render(request,'update_product.html',{'data':data})
    return redirect(login)

def delete_product(request,d):
    if 'admin' in request.session:
        data = product.objects.get(pk=d)
        data.delete()
        messages.error(request,'Cake deleted')
        return redirect(manage_product)
    return redirect(login)

def view_user(request):
    if 'admin' in request.session:
        data=user_register.objects.all()
        return render(request,'view_user.html',{'data':data})
    return redirect(login)

def logout(request):
    if 'user' in request.session or 'admin' in request.session:
        request.session.flush()
        return redirect(login)


def add_cart(request,d):
    if 'user' in request.session:
        data=product.objects.get(pk=d)
        print(data)
        user=user_register.objects.get(username=request.session['user'])
        print(user)
        if cart.objects.filter(product_details=data).exists():
            p=cart.objects.get(product_details=data)
            p.quantity+=1
            p.save()
            # messages.error(request,'item already exists')
        else:
            cart.objects.create(user_details=user,product_details=data,total_price=data.cake_price).save()
        return redirect(display_cart)
    return redirect(login)

def display_cart(request):
    if 'user' in request.session:
        user = user_register.objects.get(username=request.session['user'])
        data=cart.objects.filter(user_details=user)
        s1=0
        for i in data:
           s1=s1+i.total_price
        print(s1)
        request.session['cart_total']=s1
        return render(request,'display_cart.html',{'data':data,'s':s1})
    return redirect(login)
def remove_cart(request,d):
    if 'user' in request.session:
        data = cart.objects.get(pk=d)
        print(data)
        data.delete()
        messages.success(request,'Item Removed From our Cart')
        return redirect(display_cart)
    return redirect(login)

def add_wishlist(request,d):
    if 'user' in request.session:
        data=product.objects.get(pk=d)
        print(data)
        user=user_register.objects.get(username=request.session['user'])
        print(user)
        wishlist.objects.create(user_details=user,product_details=data).save()
        return redirect(display_wishlist)
    return redirect(login)

def display_wishlist(request):
    if 'user' in request.session:
        user = user_register.objects.get(username=request.session['user'])
        data=wishlist.objects.filter(user_details=user)
        return render(request,'display_wishlist.html',{'data':data})
    return redirect(login)



def remove_wishlist(request,d):
    if 'user' in request.session:
        data = wishlist.objects.get(pk=d)
        print(data)
        data.delete()
        messages.success(request,'Item Removed From our Wishlist')
        return redirect(display_wishlist)
    return redirect(login)


def increment(request,d):
    if 'user' in request.session:
        data = cart.objects.get(pk=d)
        print(data)
        if data.quantity >= 1:
            data.quantity+=1
            data.total_price=data.quantity*data.product_details.cake_price
            data.save()
            return redirect(display_cart)
    return redirect(login)

def decrement(request,d):
    if 'user' in request.session:
        data = cart.objects.get(pk=d)
        print(data)
        if data.quantity > 1:
            data.quantity-=1
            data.total_price=data.quantity*data.product_details.cake_price
            data.save()
            return redirect(display_cart)
        else:
            data.delete()
            messages.success(request,'Removed from the  Cart')
            return redirect(userhome)
    return redirect(login)


#payment

import razorpay
def payment(request,d):
        amount = d * 100
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        return render(request, "payment.html",{'amount':amount})

def success(request):
    return render(request,'success.html')

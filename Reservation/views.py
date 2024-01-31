from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from Reservation.models import Student,Item,Booking
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        uid = request.POST.get('uid')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        allstudent = Student.objects.filter(uid=uid).values()
        for student in allstudent:
            if student['uid']==uid:
                if pass1==pass2:
                    data=Student(uid=uid,name=name,email=email,password=pass1)
                    data.save()
                    return render(request , 'login.html')
                
        else:
            return HttpResponse ("Get ID from admin first!!")
    return render(request , 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        uid = request.POST.get('uid')
        request.session['uid'] = uid
        password = request.POST.get('password')
        allstudent = Student.objects.filter(uid=uid,password=password).values()
        for loginpass in allstudent:
            if loginpass['uid']==uid:
                if loginpass['password']==password:
                    return redirect('index')
        else:
            return HttpResponse ("ID or password invalid!!")
        
    return render (request,'login.html')

def update_password(request):
    if request.method=='POST':
        uid = request.POST.get('uid')
        old_pass = request.POST.get('old_password')
        new_pass1 = request.POST.get('new_password1')
        new_pass2 = request.POST.get('new_password2')

        # Check if the user exists
        try:
            student = Student.objects.get(uid=uid)
        except Student.DoesNotExist:
            return HttpResponse("User does not exist!!")
        
        # Verify old password
        if student.password != old_pass:
            return HttpResponse("Old password is incorrect!!")
        
        # Check if new passwords match
        if new_pass1 != new_pass2:
            return HttpResponse("New passwords do not match!!")
        
        # Update password
        student.password = new_pass1
        student.save()
        
        return HttpResponse("Password updated successfully!!")
    
    return render(request, 'update_password.html')
        

#Index
def index(request):
    if request.session.has_key('uid'):
        uid = request.session['uid']
        print(uid)
        item=Item.objects.all()    
        context= {
            'item' : item, 
            'uid' : uid,
            }
    return render (request,"index.html",context)

def outindex(request):
    if request.session.has_key('uid'):
        uid = request.session['uid']
        item=Item.objects.all()    
        context= {
            'item' : item,
            'uid' : uid,
            }
    else:
        # If uid is not present in session, set context without uid
        item=Item.objects.all()    
        context= {
            'item' : item,
            }

    return render (request,"out_index.html",context)

def product(request):
     if request.session.has_key('uid'):
        uid = request.session['uid']
        print(uid)
        item=Item.objects.all()    
        context= {
            'item' : item,
            'uid' : uid,
        }
        return render (request,"product.html",context)

def product_detail(request,slug):
    if request.session.has_key('uid'):
        uid = request.session['uid']
        item=Item.objects.filter(slug=slug).values()
        context = {
            'item' : item,
            'uid' : uid
        }
        print(uid)
        if request.method =='POST':
            itemcode = request.POST.get('itemcode')
            startdate = request.POST['startdate']
            enddate = request.POST['enddate']
            quantity= request.POST['quantity']
            booking = Booking(uid_id=uid, itemcode_id=itemcode, startdate=startdate, enddate=enddate, quantity=quantity)
            booking.save()
            return redirect(reverse('product_detail', kwargs={'slug': slug}))
        return render(request, 'product_detail.html', context)
    return render(request, 'product_detail.html')
    
def cart(request):
    if request.session.has_key('uid'):
        uid = request.session['uid']
        print(uid)
        bookings = Booking.objects.all()
        context = {'bookings': bookings,
                   'uid': uid}

    return render (request,"cart.html",context)

def delete_cart(request,itemcode):
    if request.session.has_key('uid'):
        uid = request.session['uid']
        print(uid)
        bookings = Booking.objects.filter(itemcode=itemcode)
        bookings.delete()
        return HttpResponseRedirect(reverse('cart'))
    
def delete_all(request,uid):
    if request.session.has_key('uid'):
        u_id = request.session['uid']
        print(u_id)
        bookings = Booking.objects.filter(uid=uid)
        bookings.delete()
        return HttpResponseRedirect(reverse('cart'))

def update_cart(request, booking_id):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        startdate =  request.POST['startdate']
        enddate =  request.POST['enddate']
        booking = Booking.objects.get(id=booking_id)
        booking.quantity = quantity
        booking.startdate = startdate
        booking.enddate = enddate
        booking.save()
        return redirect('cart')

    booking = Booking.objects.get(id=booking_id)
    context = {'booking': booking}
    return render(request, 'update_cart.html', context)

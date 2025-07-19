from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout
from .models import *
import random
from .utils import generate_otp, send_otp
from django.utils import timezone
import twilio

# Create your views here.

def signUp(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phoneNumber = request.POST['phone']
        password = request.POST['password']
        
        data = signUpDetail.objects.create(firstName=firstName, lastName=lastName, email=email, mobileNumber=phoneNumber, password=password)
        return redirect('login')

    return render(request, 'signup.html')

def logIn(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
                
        try:
            data = signUpDetail.objects.get(email=email)
            request.session['user_id'] = data.userId
        except signUpDetail.DoesNotExist:
            msg = {'error': "Invalid email!"}
            return render(request, 'login.html', msg)
        
        if data.password != password:
            msg={'error':"Invalid password!"}
            return render(request,'login.html',msg)
        
        else:
            return redirect('/')
        
    return render(request, 'login.html')

def logOut(request):
    logout(request)
    return redirect('index')

def forgotPassword(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        
        # data = signUpDetail.objects.get(email=email)
        
        try:
            user = signUpDetail.objects.get(mobileNumber=phone)
            otp = generate_otp()
            request.session['otp'] = otp
            request.session['uid'] = user.userId
            expires_at = timezone.now() + timezone.timedelta(minutes=10)
            OTP.objects.create(user=user, otp=otp, expires_at=expires_at)
            send_otp(phone, otp)  
            return redirect('checkOtp')
        except signUpDetail.DoesNotExist:
            msg = {'error': "Invalid phone!"}
            return render(request, 'forgotPassword.html', msg)
        
    return render(request, 'forgotPassword.html')

def checkOtp(request):
    # otp = random.randint(1000, 9999)
    if request.method == 'POST':
        verfiyOtp = request.POST['verifyOtp']
    
        checkOtp = request.session.get('otp')
        if(verfiyOtp == checkOtp):
            # print(verfiyOtp)
            del request.session['otp']
            return redirect('resetPassword')
        else:
            msg = {'error': "Check OTP"}
            return render(request, 'otp.html', msg)
            
    return render(request, 'otp.html')

def resetPassword(request):
    if request.method == 'POST':
        npassword = request.POST['npassword']
        cpassword = request.POST['cpassword']
        
        uid = request.session.get('uid')
        if npassword == cpassword:
            user = signUpDetail.objects.get(userId=uid)
            user.password = npassword
            user.save()
            del request.session['uid']
            return redirect('login')
        else:
            msg = {'error': "Password does not match"}
            return render(request, 'resetPassword.html', msg)
            
            
    return render(request, 'resetPassword.html')

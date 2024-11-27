from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import*
from library.models import books
import datetime
from django.contrib import messages
def user_register(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        gender=request.POST['gender']
        username=request.POST['username']
        password=request.POST['password']
        reg=student(name=name,age=age,address=address,gender=gender,username=username,password=password)
        reg.save()
    return render(request,'register.html')

def student_home(request):
    
    return render(request,'studenthome.html')



def view_book(request):
   a=books.objects.all()
   return render(request,'viewbook.html',{'m':a})

def book_ing(request,id):
    booking_id=id
    student_id=request.session['id'] 
    date=datetime.date.today()
    m=booking(booking_id_id=booking_id,student_id_id=student_id,booking_date=date)
    m.save()
    return redirect('view_book')
    
def reserved(request):
    student_id=request.session['id']
    book=booking.objects.filter(student_id_id=student_id,status='pending')
    return render(request,'reservedbook.html',{'bo':book})

def returned(request,id):
    date=datetime.date.today()
    book=booking.objects.filter(id=id).update(status='Returned',return_date=date)
    messages.add_message(request,messages.INFO,'book returned')
    return redirect('reserved')

def myhistory(request):
    student_id=request.session['id']
    book=booking.objects.filter(student_id_id=student_id)
    return render(request,'myhistory.html',{'bo':book})

def profile(request):
    reg=student.objects.filter(id=request.session['id'])
    return render(request,'profile.html',{'pr':reg})

def changestudent(request):
    return render(request,'changestudent.html')

def studentpassaction(request):
    if request.method=='POST':
        old_password=request.POST['old']
        new_password=request.POST['new']
        confirm_new_password=request.POST['confirm']
        if new_password==confirm_new_password:
            data=student.objects.filter(password=old_password)
            if data.count()>0:
                student.objects.filter(id=data[0].id).update(password=new_password)
                messages.add_message(request,messages.INFO,'PASSWORD UPDATED')
            else:
                messages.add_message(request,messages.INFO,'incorrect password')
                return redirect('changestudent')
        else:
            messages.add_message(request,messages.INFO,'password does not match')
            return redirect('changestudent')

def forgot(request):
    return render(request,'forgot.html')

def useraction(request):
    if request.method=='POST':
        username=request.POST['username']
        data=student.objects.filter(username=username)
        if data.count()>0:
            request.session['newid']=data[0].id
            return render(request,'userdetails.html')
        else:
            messages.add_message(request,messages.INFO,'invalid username')
            return redirect('forgot')

def detailsaction(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        data=student.objects.filter(name=name,age=age,address=address)
        if data.count()>0:
            return render(request,'finalpage.html')
        else:
            return render(request,'userdetails.html')

def finalaction(request):
    if request.method=='POST':
        id=request.session['newid']        
        new_password=request.POST['new']
        student.objects.filter(id=id).update(password=new_password)
    return render(request,'finalpage.html')






















        



   











   


















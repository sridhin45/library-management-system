from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import HttpResponse
from .models import*
from django.contrib import messages
from student.models import student
from student.models import booking

def home(request):
    return render(request,'home.html')

def index(request):
    if 'id' in request.session and 'role' in request.session:
        if request.session['role']=='librarian':
            return redirect('home')
        elif request.session['role']=='student':
            return redirect('student_home')
    return render(request,'index.html')

def login_here(request):
    if 'id' in request.session and 'role' in request.session:
        if request.session['role']==librarian:
            return redirect('login_here')
        elif request.session['role']=='student':
            return redirect('login_here')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        librarian_user=librarian.objects.filter(username=username,password=password).first()
        student_user=student.objects.filter(username=username,password=password).first()

        if librarian_user:
            request.session['id']=librarian_user.id
            request.session['role']='librarian'
            return redirect('home')
        elif student_user:
            request.session['id'] = student_user.id
            request.session['role']='student'
            return redirect('student_home')
        else:
            return redirect('login_here')
    return render(request,'login.html')
        
def add_category(request):
    if request.method=='POST':
        category=request.POST['category']
        a=categorys(name=category)
        a.save()
        messages.add_message(request,messages.INFO,"category added successfully")
    return render(request,'category.html')

def book(request):
    bo=categorys.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        author=request.POST['author']
        description=request.POST['description']
        coverphoto=request.FILES['coverphoto']
        No_of_copies=request.POST['No_of_copies']
        b=books(name=name,category_id=category,author=author,description=description,coverphoto=coverphoto,No_of_copies=No_of_copies)
        b.save()
    return render(request,'book.html',{'bo':bo})

def book_view(request):
    a=books.objects.all()
    return render(request,'bookviews.html',{'m':a})

def edit(request,id):
    p=get_object_or_404(books,id=id)
    if request.method=='POST':
        name=request.POST['name']
        category=request.POST['category']
        author=request.POST['author']
        description=request.POST['description']
        coverphoto=request.FILES['coverphoto'] if request.FILES else p.coverphoto
        No_of_copies=request.POST['No_of_copies']
        p.name=name
        p.categorys=category
        p.author=author
        p.description=description
        p.coverphoto=coverphoto
        p.No_of_copies=No_of_copies
        p.save()
        return redirect('book_view')
    m=books.objects.filter(id=id)
    bo=books.objects.all()
    return render(request,'edit.html',{'m':m,'bo':bo})

def delete(requets,id):
    m=books.objects.filter(id=id)
    m.delete()
    return redirect('book_view')

def logout(request):
        request.session.flush()
        return redirect('login_here')

def viewhistory(request):
    history=booking.objects.all()
    return render(request,'viewhistory.html',{'his':history})

def viewreturn(request):
    book=booking.objects.filter(status="Returned")
    return render(request,'viewreturn.html',{'bo':book})

def accept(request,id):
    Booking=get_object_or_404(booking,id=id)
    Booking.status='Accepted'
    Booking.save()
    Book=get_object_or_404(books, id=Booking.booking_id_id)
    Book.No_of_copies +=1
    Book.save()
    messages.add_message(request,messages.INFO,'accepted')
    return redirect('viewreturn')

def changeadmin(request):
    return render(request,'changeadmin.html')

def adminpassaction(request):
    if request.method=='POST':
       old_password=request.POST['old']
       new_password=request.POST['new']
       confirm_new_password=request.POST['confirm']
       if new_password== confirm_new_password:
            data=librarian.objects.filter(password=old_password)
            if data.count()>0:
                librarian.objects.filter(id=data[0].id).update(password=new_password)
                messages.add_message(request,messages.INFO,'password updated')
            else:
                messages.add_message(request,messages.INFO,'incorect password')
                return redirect('changeadmin')
       else:
            messages.add_message(request,messages.INFO,'pssword does not match')
    return redirect('changeadmin')


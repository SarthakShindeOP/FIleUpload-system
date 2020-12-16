from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import login,Savedfile
from django.contrib import messages
from django.contrib import sessions

# Create your views here.
def home(request):
    return render(request,'jokes.html',{'welcome':"Welcome"})

def logins(request):
    user=request.POST['username']
    password=request.POST['password']
    if user:
        match=login.objects.filter(Q(Username__iexact=user))
        if match:
            check=login.objects.filter(Q(password__iexact=password))
            if check:
                request.session['username']=user
                return render(request,'result.html',{'check':match})
            else:
                return render(request,'jokes.html',{"message":"Wrong password"})
        else:
            return render(request,'newlogin.html',{'noaccountfound':'There doesnot exist any account you can create new'})
    else:
        return render(request,'jokes.html')
def submit(request):
    user=request.session.get('username')
    if len(request.FILES) != 0:
        file=request.FILES['insert']
        save=Savedfile(Username=user,file=file)
        save.save() 
        saved=Savedfile.objects.filter(Q(Username__iexact=user) )
        return render(request,'result.html',{'userfile':saved,'upload':'file Uploaded','uploaded':'All uploaded files'})
    else:
        return render(request,'result.html',{'filenotfound':'pls insert a file '})
def newlogin(request):
    a=request.POST['username']
    password1=request.POST['password1']
    password2=request.POST['password2']
    if a:
        match=login.objects.filter(Q(Username__iexact=a))
        if match:
           return render(request,'newlogin.html',{'taken':"Username taken"}) 
        else:
            if len(password1)!=0 and len(password2)!=0: 
                if password1==password2:
                    save=login(Username=a,password=password1)
                    save.save()
                    return render(request,'jokes.html',{'created':"Account created"})
                else:
                    return render(request,'newlogin.html',{"message1":"Password didn't match"})
            else:
                return render(request,'newlogin.html')
    else:
        return render(request,'newlogin.html')
        
   

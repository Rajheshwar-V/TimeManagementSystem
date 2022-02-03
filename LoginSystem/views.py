from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
User = get_user_model()
from django.contrib import messages
    
    # Create your views here.
def home(request):
    if request.method == "POST":
         
        username = request.POST.get('username')
       
        password = request.POST.get('password')

        authUser = authenticate(
            username=username,
            password = password
            )
        if authUser is not None :
           login(request,authUser)
           return render(request,'home.html')
        else:
            messages.error(request,'Invalid Credentials')
        return render(request,'login.html')
    return render(request,'home.html')
def loginView(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
       
        username = request.POST.get('username')
         
        password = request.POST.get('password')
 
        authUser = authenticate(
            username=username,
            password = password
            )
        if authUser is not None :
           login(request,authUser)
           return redirect('/')
        else:
            messages.error(request,'Invalid Credentials')
        return render(request,'login.html')
    return render(request,'login.html')
 
def register(request):
    u = User()
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
            
        createNewUser = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
            password = password,
             
    
        )
        createNewUser.save()
            
          
        return redirect('/')
        
    return render(request,'register.html')
def logoutView(request):
    logout(request)
    return redirect('/')

def changePassword(request):
    if request.user.is_authenticated:
        username = request.user.username
        if request.method == 'POST':
            newpassword = request.POST.get('password')
            u = User.objects.get(username=username)
            u.set_password(newpassword)
            u.save()
            messages.success(request,'Password Chnaged Please login with new password')
            return render(request,'login.html')
             
    
            
            
    return render(request,'chnagepassword.html')
  

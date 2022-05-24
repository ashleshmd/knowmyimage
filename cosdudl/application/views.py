from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
# Create your views here.

def login_page(request):
    return render(request,'application/profile.html')
def home(request):
    return render(request,'application/index.html')
def inner_page(request):
    return render(request,'application/inner-page.html')

def login(request):
    if request.method == 'POST':
        login_name = request.POST['username']
        login_password = request.POST['password']
        # print(login_name,login_password)
        user = authenticate(username=login_name, password=login_password)
        if user is None:
            return redirect("login")
        else:
            auth_login(request, user)
            return redirect("inner-page")

#
#
# from msilib.schema import File
#
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
#
# from django.contrib.auth import authenticate, logout
# from django.contrib.auth import login as auth_login
# from PIL import Image
#
# # from .forms import ProfileImage
# from .models import Profile
# def login_page(request):
#         return render(request,'application/login.html')
#
#
# def inner_page(request):
#     return render(request, 'application/index.html',{'user':request.user})
#
# def index(request):
#     if request.method == 'POST':
#         login_name = request.POST['username']
#         login_password = request.POST['password']
#         user = authenticate(username=login_name, password=login_password)
#         if user is None:
#             return redirect("login_page")
#         else:
#             auth_login(request, user)
#             return redirect("home2")
#
# def handlelogout(request):`
#     logout(request)
#     return render(request,'application/login.html')
#
#
# def books(request):
#     return render(request,'application/books.html')
#
#
# def profile(request):
#     profile = Profile.objects.get(user = request.user)
#     return render(request,'application/profile.html',{'user':request.user,'profile':profile})
#
# def reset_password(request):
#     profile = Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         password = request.POST['current_password']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         u = request.user
#         if password1 == password2 and u.check_password(password):
#             u.set_password(password1)
#             u.save()
#             authenticate(username=u, password=password1)
#         return render(request, 'application/profile.html', {'user': request.user, 'profile': profile})
#     else:
#         return render(request, 'application/reset_password.html', {'user': request.user, 'profile': profile})
#
#
#
#
# def edit_profile(request):
#     p = Profile.objects.get(user=request.user)
#     if request.method == 'POST':
#         email = request.POST['email']
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         usn = request.POST['usn']
#         branch = request.POST['branch']
#         section = request.POST['section']
#         locality = request.POST['locality']
#         image = request.FILES['profile_image']
#         p.profile_image.delete()
#         p.profile_image.save(image.name, image)
#         user = request.user
#         pr = Profile.objects.get(user=user)
#         user.username = username
#         user.first_name = first_name
#         user.last_name = last_name
#         user.email = email
#         user.save()
#         pr.usn = usn
#         pr.branch = branch
#         pr.section = section
#         pr.locality = locality
#         pr.save()
#         return render(request,'application/profile.html', {'user':request.user,'profile':p})
#     else:
#          return render(request, 'application/edit_profile.html',{'user':request.user,'profile':p})
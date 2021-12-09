from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.serializers import Serializer
from django.http import JsonResponse
from demo.serializers import StudentSerializers
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, logout as userLogout,login as userLogin
from django.contrib import messages
# Create your views here.


# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     Serializer_class = StudentSerializers
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]

def index(request):
    return render(request,'index.html')


# @api_view(['GET'])
# @permission_classes([IsAdminUser])   #IsAuthenticated  AllowAny
def administrator(request):
    if request.user.is_superuser:
       return render(request, 'superuser.html')
    else:
        messages.info(request,'u r not superUser')
        return render(request,'profile.html')


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])   #IsAdminUser  AllowAny
def authenticUser(request):
    if request.user.is_authenticated:
       return render( request,'authenticUser.html')

def login(request):
    # if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username, password = password)

    if user is not None:
        userLogin(request,user)
        # return HttpResponse('u r logged in successfully')
        return render(request,'profile.html')
    else:
        # message.info(request, 'invalid credentials')
        return redirect('login')


def loginPage(request):
        # if request.method == 'GET':
    return render(request,'login.html')

def logout(request):
    userLogout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        is_staff = (request.POST['operator']) 
        if   is_staff == 'on':
            is_staff = "True"
        else:
            is_staff= "False"
        user = User.objects.create_user(username=username, first_name = first_name,last_name=last_name,email=email,password=password, is_staff= is_staff)
        user.save()
        print("user created!!")
        return redirect("/")      

    else:
        return render(request,'Register.html')





# class Register(APIView):
#     def post(self,request):
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         user = User.objects.create_user(username=username, first_name = first_name,last_name=last_name,email=email,password=password)
#         user.save()
#         print("user created!!")
#         return redirect('/')
#         # return Response({'success': True})

# class UserLogin(APIView):
#     def post(self, request):
#         data=request.data
#         if(User.objects.filter(username=data['username'],password=data['password']).exists()):
#             status={ 'success': True, 'name': data['user_name']}
#             return Response(status)
#         return Response({'success': False, 'message':'invalid username or pasword'})

class GetUserInfo(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]   #IsAuthenticated  AllowAny  
    def get(self,request):
        
        return Response({'success': False, 'message':'invalid username or pasword'})
        


# git add .
# git commit -m "message"
# git push origin main
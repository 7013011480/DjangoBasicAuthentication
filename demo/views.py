from django.shortcuts import redirect, render
from rest_framework.serializers import Serializer
from django.http import JsonResponse
from demo.serializers import StudentSerializers
from .models import Student
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
# Create your views here.


# class StudentModelViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     Serializer_class = StudentSerializers
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]

def index(request):
    return render(request,'index.html')

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

class UserLogin(APIView):
    def post(self, request):
        data=request.data
        if(User.objects.filter(username=data['user_name'],password=data['password']).exists()):
            status={ 'success': True, 'name': data['user_name']}
            return Response(status)
        return Response({'success': False, 'message':'invalid username or pasword'})

class GetUserInfo(APIView):
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]   #IsAuthenticated  AllowAny  
    def get(self,request):
        
        return Response({'success': False, 'message':'invalid username or pasword'})
        
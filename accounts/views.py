

from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from django.shortcuts import  render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .serializers import SingUpSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


# Create your views here.
def redirect_login(request):
    return redirect('login')

def login(request):
    if not 'username' in request.session:
        if request.method =='POST':
            username=request.POST['username']
            password=request.POST['password']
            # return HttpResponse(username+' '+password)

            if username == '' or password == '':
                        return render(request,'login.html',{'error':'رجاءً قم بملء جميع الحقول'})

            for user in User.objects.all():

                if check_password(password, user.password) and username == user.username and user.is_staff == 1:
                    request.session['username'] = username
                    return redirect('home')
                # str(user.username)==str(username) and str(user.password)==str(make_password(password)):
                
                #     return redirect('menu/')
            

            return render(request,'login.html',{'error':'اسم المستخدم او كلمة المرور غير صيحية'})
    
        return render(request,'login.html')
    
    return redirect('home')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')
        
    
   
@api_view(['POST'])
def sign_up(request):
    data = request.data
    user = SingUpSerializer(data = data)

    if user.is_valid():
        if not User.objects.filter(username=data['username']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'], 
                email = data['email'] , 
                username = data['username'] , 
                password = make_password(data['password']),
            )
            return Response(
                {'details':'Your account registered susccessfully!' },
                    )
        else:
            return Response(
                {'eroor':'This username already exists!' },
                    status=status.HTTP_400_BAD_REQUEST
                    )
    else:
        return Response(user.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = UserSerializer(request.user, many=False)
    return Response(user.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    user = request.user
    data = request.data

    
    if 'first_name' in data and 'last_name' in data and 'username' in data \
    and 'email' in data and 'password' in data:
        
        if data['first_name'] =='' or data['username'] =='' or \
            data['last_name'] == ''  or data['email'] == '' or data['password'] =='' :
             return Response({'error':'رجاءً قم بملء جميع الحقول'},status=status.HTTP_400_BAD_REQUEST)
        
        user.first_name = data['first_name']
        user.username = data['username']
        user.last_name = data['last_name']
        user.email = data['email']
        user.password =  make_password(data['password'])
        user.save()
        serializer = UserSerializer(user,many=False)
        return Response(serializer.data)

    
    else:
         return Response({'error':'جميع الحقول مطلوبة'},status=status.HTTP_400_BAD_REQUEST)



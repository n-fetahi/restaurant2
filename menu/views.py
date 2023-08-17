
from email.mime import image
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import *
import os
from PIL import Image
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from .serializers import MenuSerializer
from .filters import MenuFilter

# Create your views here.



def home(request):


    if 'username' in request.session:
        if 'c' in request.GET:
            
            if request.GET['c'] == '2':
                drinks =Menu.objects.filter(category='drinks',state=1).values()
                return render(request,'index.html',{"meals":drinks})

            elif request.GET['c'] == '3':
                sweet =Menu.objects.filter(category='sweet',state=1).values()
                return render(request,'index.html',{"meals":sweet})
        
        
        foods =Menu.objects.filter(category='foods',state=1).values()
        return render(request,'index.html',{"meals":foods})
    return render(request,'error-template.html',{"error_text":'خطأ في طلب الصفحة'})
    


def meal_details(request):
    if 'username' in request.session:
        if 'i' in request.GET :
            chek_meal=Menu.objects.filter(id =int(request.GET['i'])).exists()
            if not chek_meal:
              return render(request,'error-template.html',{'error_text':'عذراً قم بإختيار العتصر أولاً'})
            meal=Menu.objects.get(id =int(request.GET['i']))
            request.session['categoray']=int(request.GET['i'])
            return render(request,'meal_details.html',{'meal':meal})

        return redirect('home')
    
    return render(request,'error-template.html',{"error_text":'خطأ في طلب الصفحة'})


def add_meal(request):
    if 'username' in request.session:
        if request.method == "POST":

            if request.POST['meal_name'] == '' or request.POST['price'] == '' \
                or request.FILES['image'] == ''  or request.POST['describe'] == '' \
                or request.POST['category'] == '':
                meal={
                    'meal_name':request.POST['meal_name'],
                    'price':request.POST['price'],
                    'describe':request.POST['describe']
                }

                return render(request,'add_meal.html',{
                    'error_msg':'رجاءً قم بملء جميع الحقول',
                    'meal':meal
                    })
                    
            if not Menu.objects.filter(meal_name=request.POST['meal_name']).exists():
                # if os.path.exists("media/menu_images/") is True:

                Menu.objects.create(
                meal_name=request.POST['meal_name'],
                price=request.POST['price'],
                image=request.FILES['image'],
                describe=request.POST['describe'],
                category=request.POST['category'],
                )
                return render(request,'add_meal.html',{'success_msg':'تمت إضافة الوجبة بنجاح'})
            else:
                return render(request,'add_meal.html',{'error_msg':'هذه الوجبة موجودة من قبل'})

        return render(request,'add_meal.html')
    return render(request,'error-template.html',{"error_text":'خطأ في طلب الصفحة'})

def update_meal(request):
    if 'username' in request.session:
        if 'categoray' in request.session:

            meal=Menu.objects.get(id =request.session['categoray'])
            if request.method == 'POST':

                if request.POST['meal_name'] == '' or request.POST['price'] == '' \
                    or request.POST['describe'] == '' \
                    or request.POST['category'] == '':
                    
                    meal={
                        'meal_name':request.POST['meal_name'],
                        'price':request.POST['price'],
                        'describe':request.POST['describe']
                    }

                    return render(request,'update_meal.html',{
                        'error_msg':'رجاءً قم بملء جميع الحقول',
                        'meal':meal
                        })
                        
                meal.meal_name=request.POST['meal_name']
                meal.price=request.POST['price']
                meal.describe=request.POST['describe']
                meal.category=request.POST['category']

                if 'image' in request.POST :
                    meal.image=meal.image
                    
                else:    
                    meal.image=request.FILES['image']


                meal.save()
                return render(request,'meal_details.html',{'meal':meal})
            else:

                return render(request,'update_meal.html',{'meal':meal})
        else:
            return render(request,'error-template.html',{'error_text':'عذراً قم بإختيار العتصر أولاً'})
    return render(request,'error-template.html',{"error_text":'خطأ في طلب الصفحة'})

def delete_meal(request):
    if 'categoray' in request.session:
        meal=Menu.objects.get(id =request.session['categoray'])
        meal.state=0
        meal.save()
    
        return redirect('home')
@api_view(['GET'])  
def all_menu(request):

    menu_filter=MenuFilter(request.GET,queryset=Menu.objects.filter(state=1))
    
    page_size=5
    paginator=PageNumberPagination()
    paginator.page_size=page_size
    qu_set=paginator.paginate_queryset(menu_filter.qs,request)

    menu_ser=MenuSerializer(qu_set,many=True)
    return Response({'menu':menu_ser.data,
                     'page_saie':page_size,
                     'count':menu_filter.qs.count()
                     },)

@api_view(['GET'])
def get_meal_by_ID(request,search_id):
    meal = get_object_or_404(Menu,id=search_id)
    menu_ser=MenuSerializer(meal,many=False)
    
    return Response({'menu':menu_ser.data})
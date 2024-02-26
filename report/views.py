from django.shortcuts import render,redirect,get_object_or_404,get_object_or_404,HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users
from store.models import *
from custom.utils import getMonthName
from django.http import JsonResponse
from django.db.models import Sum, F
from django.utils import timezone
import datetime

@login_required()
def ReporttypeData(request):
    data_type = Category.objects.all()
    loopingCategoory = []
    for category in data_type.iterator():
        total1 = Order.objects.filter(product__category_id=category.id, is_sent=True).count()
        total2 = Order.objects.filter(product__category_id=category.id, status=True,is_sent=False).count()
        total3 = Order.objects.filter(product__category_id=category.id, status=False ,is_sent=False).count()
        loopingCategoory.append({
            'id': category.id,
            'name': category.name,
            'total1': total1,
            'total2': total2,
            'total3': total3,
        })
    today = datetime.date.today()
    dadus_tinan_agora = []
    totalProductPaidMoth = 0
    totalproductProcessA = 0
    totalproductPandingA = 0

    for i in range(12):
        monthName = getMonthName(i+1)
        totalproductPaid = Order.objects.filter(date__month=i+1,date__year=today.year,status=True, is_sent=True, is_approved=True).all()
        totalOsanPaid = 0
        for x in totalproductPaid:
            totalOsanPaid += x.price * x.quantity
            totalProductPaidMoth += x.price * x.quantity
        totalproductProcess = Order.objects.filter(date__month=i+1,date__year=today.year, status=True, is_sent=False).all()
        totalOsanProcess = 0
        for x in totalproductProcess:
            totalOsanProcess += x.price * x.quantity
            totalproductProcessA += x.price * x.quantity

        totalproductPanding = Order.objects.filter(date__month=i+1,date__year=today.year, status=False, is_sent=False).all()
        totalOsanPanding = 0
        for x in totalproductPanding:
            totalOsanPanding += x.price * x.quantity
            totalproductPandingA += x.price * x.quantity

        dadus_tinan_agora.append([i+1,monthName,totalOsanPaid,totalOsanProcess,totalOsanPanding])
    dadus_tinan_agora.append(["","Total",totalProductPaidMoth,totalproductProcessA,totalproductPandingA])

    # Sumariu tuir tinan
    dadus_pakote_tuir_tinan = []
    totalProductPaidMoth = 0
    totalproductProcessA = 0
    totalproductPandingA = 0

    totalproductPaidY = Order.objects.filter().distinct().values('date__year').all().order_by('-date__year')
    for tinan in totalproductPaidY:
        totalproductPaid = Order.objects.filter(date__year=tinan['date__year'],status=True, is_sent=True, is_approved=True).all()
        totalPakotepaid = 0
        for x in totalproductPaid:
            totalPakotepaid += x.price * x.quantity
            totalProductPaidMoth += x.price * x.quantity
        totalProductProcess = Order.objects.filter(date__year=tinan['date__year'],status=True, is_sent=False).all()
        totalMoneyProcess = 0
        for x in totalProductProcess:
            totalMoneyProcess += x.price * x.quantity
            totalproductProcessA += x.price * x.quantity

        totalMoneyPanding = Order.objects.filter(date__year=tinan['date__year'],status=False, is_sent=False).all()
        totalMPannding = 0
        for x in totalMoneyPanding:
            totalMPannding += x.price * x.quantity
            totalproductPandingA += x.price * x.quantity
        dadus_pakote_tuir_tinan.append([tinan['date__year'],totalPakotepaid,totalMoneyProcess,totalMPannding])
    dadus_pakote_tuir_tinan.append(["Total",totalProductPaidMoth,totalproductProcessA,totalproductPandingA])
    context = {
        "data_type": data_type,
        "loopingCategoory": loopingCategoory,
        "currentYear":today.year,
        "dadus_tinan_agora":dadus_tinan_agora,
        "dadus_pakote_tuir_tinan":dadus_pakote_tuir_tinan,

    }

    return render(request, 'report/category.html', context)

def total_price_per_product_by_month(request):
    tinanorderprice = Order.objects.filter().distinct().values('date__year').all().order_by('-date__year')
    loopingpriceeyears=[]
    for ii in tinanorderprice.iterator():
        total1=Order.objects.filter(date__year=ii['date__year'], is_sent=True,).aggregate(Sum('price')).get('price__sum') 
        loopingpriceeyears.append({'date__year':ii['date__year'],
            'total1':total1,
            })

        
    context ={
        "title":f"Pajina Relatoriu ho formatu Grafiku",
        "report_active":"active",
        "tinanorderprice":tinanorderprice,
        "loopingpriceeyears":loopingpriceeyears,
    }
    return render(request, "report/total_price_per_month.html",context)

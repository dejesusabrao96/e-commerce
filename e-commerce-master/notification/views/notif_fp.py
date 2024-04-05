from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
# from ukl.utils import *
from django.contrib import messages
from users.decorators import allowed_users
from store.models import *


@login_required
@allowed_users(allowed_roles=['admin'])
def adOrderNotifList(request):
	group = request.user.groups.all()[0].name
	obj1 = Order.objects.filter(status=False).all()
	# objects = obj1
	context = {
		"title":"Lista Notifikasaun Order Foun",
		"obj1":obj1,
		"group":group,
		"page":"list",
	}

	return render (request, 'lista/notif_order_list.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def notifDetailOrder(request,hashid):
	group = request.user.groups.all()[0].name
	obj1 = Order.objects.get(id=hashid)
	objects = obj1
	context = {
		"title":"Detallu Notifikasaun Orders ",
		"objects":objects,
		"group":group,
		"page":"detail",
	}

	return render (request, 'lista/notif_ecomers_detail.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def aprovaOders(request,hashid):
	OrderData = get_object_or_404(Order,id=hashid)
	OrderData.status = True
	OrderData.is_sent = False
	OrderData.is_approved = True
	OrderData.save()
	messages.success(request, f'Dadus Orders Aprova ho Susesu.')
	return redirect('notifDetailOrder',OrderData.id)


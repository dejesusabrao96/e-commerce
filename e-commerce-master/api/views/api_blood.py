import datetime
from django.db.models import Count, Q
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from custom.utils import getMonthName
from store.models import *

class ApiProductPaidMonthYear(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		today = datetime.date.today()
		label,obj1,obj2 = list(),list(),list()
		for i in range(12):
			monthName = getMonthName(i+1)
			label.append(monthName)
			totalosanperfulan = Order.objects.filter(date__month=i+1, date__year=today.year, status=True, is_sent=True, is_approved=True).all()
			totalPakoteTama = 0
			for x in totalosanperfulan:
				totalPakoteTama += x.price * x.quantity
			obj1.append(totalPakoteTama)	

			totalprocess = Order.objects.filter(date__month=i+1,date__year=today.year, status=True, is_sent=False).all()
			totprocess = 0
			for x in totalprocess:
				totprocess += x.price * x.quantity
			obj2.append(totprocess)
			
		data = { 'label': label, 'obj1': obj1,'obj2': obj2,'obj1a': "hola Ona $$.",'obj2a': "Process $$.", }
		return Response(data)

class ApiProductPaidPerYear(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]
	def get(self, request, format=None):
		group = request.user.groups.all()[0].name
		today = datetime.date.today()
		# ran tama Uza tuir fulan
		label,obj1,obj2,obj3 = list(),list(),list(),list()
		tinanProduct = Order.objects.filter().distinct().values('date__year').all().order_by('-date__year')
		for tinan in tinanProduct:
			totalMoneyPaid = Order.objects.filter(date__year=tinan['date__year'],status=True, is_sent=True, is_approved=True).all()
			totalMPaid = 0
			for x in totalMoneyPaid:
				totalMPaid += x.price * x.quantity
			obj1.append(totalMPaid)

			totalProductProcess = Order.objects.filter(date__year=tinan['date__year'],status=True, is_sent=False).all()
			totalMoneyProcess = 0
			for x in totalProductProcess:
				totalMoneyProcess += x.price * x.quantity
			obj2.append(totalMoneyProcess)

			totalproductPanding = Order.objects.filter(date__year=tinan['date__year'],status=False, is_sent=False).all()
			totalMoneyPannding = 0
			for x in totalproductPanding:
				totalMoneyPannding += x.package
			obj3.append(totalMoneyPannding)
			
			label.append(tinan['date__year'])
		data = {'label': label, 'obj1': obj1, 'obj2': obj2, 'obj3': obj3, 'obj1a': "Paid", 'obj2a': "Process", 'obj3a': "Panding"}
		return Response(data)
			


		


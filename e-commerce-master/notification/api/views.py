from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from store.models import *
# from ukl.utils import *


# # admini Notif
class APINotifBadgeadmin(APIView):
	def get(self, request, format=None):
		# fun = c_user_fun(request.user)
		obj1 = Order.objects.filter(status=False).count()
		objects = obj1
		return Response({'value':objects})


class APINotifSurveyRejeitaduFunPost(APIView):
	def get(self, request, format=None):
		# fun = c_user_fun(request.user)
		obj1 =  Order.objects.filter(status=False).count()
		objects = obj1
		return Response({'value':objects})		
# notif cosutmer
class APINotifBadgeCostumer(APIView):
	def get(self, request, format=None):
		# fun = c_user_fun(request.user)
		obj1 = Order.objects.filter(status=True).count()
		objects = obj1
		return Response({'value':objects})


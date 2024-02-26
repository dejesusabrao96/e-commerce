from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
# from ukl.utils import *
from django.contrib import messages
from users.decorators import allowed_users
# from ukl.models import *


@login_required
@allowed_users(allowed_roles=['dir_mun'])
def DMSurveyNotifList(request):
	group = request.user.groups.all()[0].name
	diretor = c_user_fun(request.user)
	obj1 = SurveyUKL.objects.filter(is_sent=True, is_approved=False,municipality__id=diretor.areamunicipality.id).all()
	objects = obj1
	context = {
		"title":"Lista Notifikasaun Kostumers",
		"objects":objects,
		"group":group,
		"page":"list",
	}

	return render (request, 'dir_mun/notif_survey_list.html',context)


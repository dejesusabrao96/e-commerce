from django.urls import path
from . import views

urlpatterns = [ 
    # adminpostu
    path('badge/dir/mun/', views.APINotifBadgeCostumer.as_view()),
    path('badge/funsionariu/postu/', views.APINotifBadgeadmin.as_view()),
    path('survey/rejeitadu/funsionariu/postu/', views.APINotifSurveyRejeitaduFunPost.as_view()),

 
]
from django.urls import path
from . import views

urlpatterns = [
    path('admin/order/notif/list/', views.adOrderNotifList, name="adOrderNotifList"),
    path('admin/order/notif/detail/<str:hashid>', views.notifDetailOrder, name="notifDetailOrder"),
    path('dir/mun/survey/approved/<str:hashid>', views.aprovaOders, name="aprovaOders"),
   
    
   
]
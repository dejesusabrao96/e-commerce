from django.contrib import admin
from django.urls import path
from .views.home import Index , store,daftar_notifikasi,aprovaOderscostumers,notifDetailOrderCostumers
from .views.signup import Signup
from .views.login import Login , logout
from .views.home import aprovaOderscostumers 
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import *
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('daftar/', daftar_notifikasi, name='daftar_notifikasi'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('costumers/order/notif/detail/<str:hashid>', notifDetailOrderCostumers, name="notifDetailOrderCostumers"),
    path('costumer/approved/<str:hashid>', aprovaOderscostumers, name="aprovaOderscostumers"),

    # path('order/sent/<str:hashid>', Sentorder, name="Sentorder"),

]

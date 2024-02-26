from django.urls import path
from . import views
from .views import *
urlpatterns = [
	path('home/',views.index,name="home"),
	path('lista-sasan/', ListaSasan, name="ListaSasan"),
	path('adsiona-sasan/', addproduct, name="addproduct"),
	path('Lista-order/', ListaOrder, name="ListaOrder"),
	path('Update-Produto/<str:hashid>', updateProduct, name="updateProduct"),
	path('delete-order/<str:id_order>', DeleteOrders, name="DeleteOrders"),
	path('delete-Produtu/<str:id_order>', DeleteProduct, name="DeleteProduct"),
	
	path('customer-list/', customer_list, name='customer_list'),
	path('customer/<int:customer_id>/', customer_detail, name='customer_detail'),
	
	path('Category-list/', Categgory_list, name='Categgory_list'),
	path('delete-Category-list/<str:id_category>', DeleteCateory, name='DeleteCateory'),
	path('update-Category-list/<str:hashid>', updatecategory, name='updatecategory'),
	path('Add-Category-list/', addCategory, name='addCategory'),

	path('categoria-Produto/<str:pk>/',catProductList, name="catProductList"),
	# path('home-login/', homelogin, name="home-login"),
]
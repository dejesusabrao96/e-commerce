from django.urls import path
from . import views

urlpatterns = [	
	path('g/product-is-paid/stock/bank/this-year/', views.ApiProductPaidMonthYear.as_view(), name="api-product-is-paid-this-year"),
	path('g/product-is-paid-process-pandig/stock/bank/by-year/', views.ApiProductPaidPerYear.as_view(), name="api-product-is-paid-process-panding-by-year"),
	
]
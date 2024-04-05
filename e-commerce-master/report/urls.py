from django.urls import path
from . import views

urlpatterns = [
    path('Report-lista-tipu-sasan/', views.ReporttypeData, name="ReporttypeData"),
    path('report/', views.total_price_per_product_by_month, name='category_report'),

]
from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models import *

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(products)
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
    # Hitung jumlah notifikasi baru
        jumlah_notifikasi_baru = Order.objects.filter(customer=customer, status=True, is_sent=False).count()
        print(jumlah_notifikasi_baru)
        return render(request , 'cart.html' , {'products' : products,'jumlah_notifikasi_baru':jumlah_notifikasi_baru } ) 


# class Cart(View):
#     def get(self, request):
#         cart = request.session.get('cart', {})
        
#         if not cart:
#             cart = {}

#         ids = list(cart.keys())

#         try:
#             products = Products.get_products_by_id(ids)
#         except Exception as e:
#             # Tangkap eksepsi jika ada kesalahan saat mengambil produk
#             print(f"Error fetching products: {e}")
#             products = []

#         try:
#             jumlah_notifikasi_baru = Order.objects.filter(status=True).count()
#         except Exception as e:
#             # Tangkap eksepsi jika ada kesalahan saat menghitung jumlah notifikasi baru
#             print(f"Error counting notifications: {e}")
#             jumlah_notifikasi_baru = 0

#         return render(request, 'cart.html', {'products': products, 'jumlah_notifikasi_baru': jumlah_notifikasi_baru})

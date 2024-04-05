from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        # Hitung jumlah notifikasi baru
        jumlah_notifikasi_baru = Order.objects.filter(customer=customer, status=True, is_sent=False).count()
        
        return render(request, 'orders.html', {'orders': orders, 'jumlah_notifikasi_baru': jumlah_notifikasi_baru})
# # Send orders ba admin
# # @login_required
# # @allowed_users(allowed_roles=['admin','admpost'])
# def Sentorder(request,hashid):
#     # group = request.user.groups.all()[0].name
#     objects = get_object_or_404(Order,hashed=hashid)
#     objects.is_sent = True
#     objects.save()
#     messages.success(request, f'ita manda onsa sasan neebe ita  atu hola ba admin ho Susesu.')
#     return redirect('DetailSurveyUKL',objects.hashed)

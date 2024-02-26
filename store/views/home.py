from django.shortcuts import render,redirect, get_object_or_404,HttpResponseRedirect
from store.models import *
from django.contrib import messages
# from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    customer = request.session.get('customer')
    orders = Order.get_orders_by_customer(customer)
    # Hitung jumlah notifikasi baru
    jumlah_notifikasi_baru = Order.objects.filter(customer=customer, status=True, is_sent=False).count()
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories
    data['jumlah_notifikasi_baru'] = jumlah_notifikasi_baru
    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

def daftar_notifikasi(request):
    customer = request.session.get('customer')
    orders = Order.get_orders_by_customer(customer)
    # Hitung jumlah notifikasi baru
    jumlah_notifikasi_baru = Order.objects.filter(customer=customer, status=True, is_sent=False).count()
    notifikasi = Order.objects.filter(customer=customer, status=True, is_sent=False).all()
    return render(request, 'ListaNotifikasaun.html', {'notifikasi': notifikasi, 'jumlah_notifikasi_baru': jumlah_notifikasi_baru})

def notifDetailOrderCostumers(request,hashid):
  obj1 = Order.objects.get(id=hashid)
  objects = obj1
  context = {
      "title":"Detallu Notifikasaun Orders ",
      "objects":objects,
      "page":"detail",
  }

  return render (request, 'NotifCostumers/notif_cistumers_detail.html',context)

def aprovaOderscostumers(request,hashid):
    OrderData = get_object_or_404(Order,id=hashid)
    OrderData.status = True
    OrderData.is_sent = True
    OrderData.is_approved = True
    OrderData.save()
    messages.success(request, f'Dadus Orders Aprova ho Susesu.')
    return redirect('notifDetailOrderCostumers',OrderData.id)




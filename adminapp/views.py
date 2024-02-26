from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from users.decorators import allowed_users
from django.db.models import Sum, Count
from django.shortcuts import render
from store.models import *
from .forms import *

# Create your views here.
@login_required
def index(request):
	# conutNotif = Order.objects.filter(status=False).count()
	context = {
		# 'conutNotif':conutNotif,
		}
	return render(request, 'home/index.html',context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def ListaSasan(request):
	group = request.user.groups.all()[0].name
	produto = Products.objects.all()
	context = {
		'group':group,
		'produto':produto,
		'sukuActive':"active",
		"page":"list",
		'title':"Lista Sasan",
	}
	return render(request,'produto/listaSasan.html',context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def addproduct(request):
    group = request.user.groups.all()[0].name
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            cl = instance.name
            instance.save()
            
            messages.success(request, f'Product {cl} is Added Successfully.')
            
            if 'save_and_add_other' in request.POST:
                # Logika untuk "Save and Add Other"
                form = ProductForm()
            else:
                return redirect('ListaSasan')
    else:
        form = ProductForm()
    
    context = {
        'group': group,
        'aldeiaActive': 'active',
        'page': 'form',
        'form': form,
    }
    
    return render(request, 'produto/listaSasan.html', context)


@login_required()
@allowed_users(allowed_roles=['admin'])
def updateProduct(request,hashid):
	group = request.user.groups.all()[0].name
	ProductData = get_object_or_404(Products,id=hashid)
	if request.method == 'POST':
		form = ProductForm(request.POST,instance=ProductData)
		if form.is_valid():
			instance = form.save()
			messages.info(request, f'Product {ProductData.name}  is updated Successfully.')
			return redirect('ListaSasan')
	else:
		form = ProductForm(instance=ProductData)
	context = {
		'page':"form",
		'group': group, 
		'form': form, 
		'ProductData': ProductData, 
	}
	return render(request, 'produto/listaSasan.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def ListaOrder(request):
	group = request.user.groups.all()[0].name
	order = Order.objects.filter(status=True).all()
	context = {
		'group':group,
		'order':order,
		'sukuActive':"active",
		"page":"list",
		'title':"Lista Order Sasan",
	}
	return render(request,'produto/listaOrder.html',context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def DeleteProduct(request, id_order):
    cl = get_object_or_404( Products, id=id_order)
    product_name = cl.name 
    cl.delete()
    messages.warning(request, f'Product {product_name} is Deleted Successfully.')
    return redirect('ListaSasan')

@login_required()
@allowed_users(allowed_roles=['admin'])
def DeleteOrders(request, id_order):
    cl = get_object_or_404( Order, id=id_order)
    order_name = cl.customer 
    cl.delete()
    messages.warning(request, f'order {order_name} is Deleted Successfully.')
    return redirect('ListaOrder')

# Lista Costumer
@login_required
@allowed_users(allowed_roles=['admin'])
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'produto/Costumers/customer_list.html', {'customers': customers})

@login_required
@allowed_users(allowed_roles=['admin'])
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    orders = Order.objects.filter(customer=customer)
    context = {
        'customer': customer, 'orders': orders,
       
    }
    return render(request, 'produto/Costumers/customer_detail.html', context)

# Lista Category
@login_required
@allowed_users(allowed_roles=['admin'])
def Categgory_list(request):
    prodto_categoria = Category.objects.all()
    prodto = Products.objects.all()
    return render(request, 'produto/category_list.html', {'prodto_categoria': prodto_categoria, 'page':'form', "page":"list",'prodto':prodto,})

@login_required
@allowed_users(allowed_roles=['admin'])
def catProductList(request, pk):
	group = request.user.groups.all()[0].name 
	prodto_categoria = Category.objects.all()
	tin = get_object_or_404(Category, pk=pk)
	prodto = Products.objects.filter(category=tin).all().order_by('-name')
	context = {'prodto': prodto,  'group': group,"page":"list",
		'title': 'Lista categoria Produto ',
		'legend': f'Lista categoria Produto {tin.name}',
		'prodto_categoria': prodto_categoria, 
	}
	return render(request, 'produto/category_list.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def DeleteCateory(request, id_category):
    cl = get_object_or_404( Category, id=id_category)
    cateegory_name = cl.name 
    cl.delete()
    messages.warning(request, f'Category {cateegory_name} is Deleted Successfully.')
    return redirect('Categgory_list')

@login_required()
@allowed_users(allowed_roles=['admin'])
def addCategory(request):
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        form =  categoriform(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            cl = instance.name
            instance.save()
            
            messages.success(request, f'Category Product {cl} is Added Successfully.')
            
            if 'save_and_add_other' in request.POST:
                # Logika untuk "Save and Add Other"
                form =  categoriform()
            else:
                return redirect('Categgory_list')
    else:
        form =  categoriform()
    
    context = {
        'group': group,
        'page': 'form',
        'form': form,
    }
    
    return render(request, 'produto/category_list.html', context)


@login_required()
@allowed_users(allowed_roles=['admin'])
def updatecategory(request,hashid):
	group = request.user.groups.all()[0].name
	ProductData = get_object_or_404(Category,id=hashid)
	if request.method == 'POST':
		form = categoriform(request.POST,instance=ProductData)
		if form.is_valid():
			instance = form.save()
			messages.info(request, f'Categori sasan {ProductData.name}  is updated Successfully.')
			return redirect('Categgory_list')
	else:
		form = categoriform(instance=ProductData)
	context = {
		'page':"form",
		'group': group, 
		'form': form, 
		'ProductData': ProductData, 
	}
	return render(request, 'produto/category_list.html', context)
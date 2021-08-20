from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.contrib import messages

# Create your views here.
def website(request):
    title="Allifmaal Website"
    context={
        "title": title
        }
    return render(request,'website.html',context)

def dashboard(request):
    title="Allifmaal Dashboard"
    header="Allifmaal Dashboard"
    context={
        "title": title,
        "header":header,
        }
    return render(request,'dashboard.html',context)

def basedashboard(request):
    title="Allifmaal Dashboard"
    context={
        "title": title,
        }
    return render(request,'base_dashboard.html',context)
def base_eshop(request):
    title="Allifmaal Online Shopping"
    context={
        "title": title,
        }
    return render(request,'eshop/base_eshop.html',context)
def stock(request):
    title="Welcome to Allifmaal stock Dashboard"
    header="Stock"
    #products = StockTable.objects.all()
    products=''
    context={
        "title": title,
        "header":header,
        "products":products,
        }
    return render(request,'stock/stock.html',context)
def hrm(request):
    title="Welcome to Allifmaal HR Dashboard"
    header="Human Resource Management"
    context={
        "title": title,
        "header":header,
        }
    return render(request,'hrm/hrm.html',context)
def customers(request):
    title="Welcome To Allifmaal Customers Dashboard"
    header="Customer Relation Management"
    context={
        "title": title,
        "header":header,
        }
    return render(request,'customers/customers.html',context)
def eshop(request):
    title="Welcome To Allifmaal Online Shopping"
    header="Allifmaal Online Shopping"
    items = ProductTable4.objects.all()
    context={
        "title": title,
        "header":header,
        "items":items,
        }
    return render(request,'eshop/eshop.html',context)
def cart(request):
    title="Welcome To Allifmaal Online Shopping"
    header="Allifmaal Online Shopping"
    context={
        "title": title,
        "header":header,
        }
    return render(request,'eshop/cart.html',context)
def checkout(request):
    title="Welcome To Allifmaal Online Shopping"
    header="Allifmaal Online Shopping"
    context={
        "title": title,
        "header":header,
        }
    return render(request,'eshop/checkout.html',context)

def stock_online(request):
    title="Allifmaal Online Stock"
    form=AddOnlineStockForm(request.POST or None)
    items = ProductTable4.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('stock_online')
   
    context={
        "title": title,
        "form":form,
        "items":items,
        
        }
    return render(request,'eshop/stock_online.html',context)

def customer_online(request):
    title="Allifmaal Online Stock"
    form=AddOnlineCustomerForm(request.POST or None)
    customers = CustomerTable4.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('customer_online')
   
    context={
        "title": title,
        "form":form,
        "customers":customers,
        
        }
    return render(request,'eshop/customer_online.html',context)
def orders_online(request):
    title="Allifmaal Online Stock"
    form=AddOnlineOrdersForm(request.POST or None)
    orders = OrderTable4.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('orders_online')
   
    context={
        "title": title,
        "form":form,
        "orders":orders,
        
        }
    return render(request,'eshop/orders_online.html',context)

def order_online_items(request):
    title="Allifmaal Online Stock"
    form=OrderOnlineItemsForm(request.POST or None)
    orderitems = OrderItemsTable4.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('order_online_items')
   
    context={
        "title": title,
        "form":form,
        "orderitems":orderitems,
        
        }
    return render(request,'eshop/order_online_items.html',context)

def shipping_address_online(request):
    title="Allifmaal Online Stock"
    form=AddShippingAdressOnlineForm(request.POST or None)
    shipping_details = ShippingAddressTable4.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('shipping_address_online')
   
    context={
        "title": title,
        "form":form,
        "shipping_details":shipping_details,
        
        }
    return render(request,'eshop/shipping_address_online.html',context)








def test(request):
    
    form=TestForm(request.POST or None)
    items = TestTable.objects.all()
    if form.is_valid():
        form.save()
        messages.success(request, 'Customer added successfully')
        return redirect('website')
   
    context={
        
        "form":form,
        "items":items,
        
        }
    return render(request,'test.html',context)








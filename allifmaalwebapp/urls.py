from django.urls import path
from . import views

urlpatterns = [
    path('',views.website,name='website'),# here do not execute index by typing index(), but just point to it by typing index
    path('dashboard/',views.dashboard,name='dashboard'),#the first 'customers' should be html name, second views name, 3rd you can change even
    path('base_dashboard/',views.basedashboard,name='base_dashboard'),
    path('stock/',views.stock,name='stock'),
    path('hrm/',views.hrm,name='hrm'),
    path('customers/',views.customers,name='customers'),
    path('eshop/',views.eshop,name='eshop'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('base_eshop/',views.base_eshop,name='base_eshop'),
    path('stock_online/',views.stock_online,name='stock_online'),
    path('customer_online/',views.customer_online,name='customer_online'),
    path('orders_online/',views.orders_online,name='orders_online'),
    path('order_online_items/',views.order_online_items,name='order_online_items'),
    path('shipping_address_online/',views.shipping_address_online,name='shipping_address_online'),


    path('test/',views.test,name='test'),
    
]
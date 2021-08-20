from django.contrib import admin


# Register your models here.
from .models import *
from .forms import *

admin.site.register(CustomerTable4)
admin.site.register(ProductTable4)
admin.site.register(OrderTable4)
admin.site.register(OrderItemsTable4)
admin.site.register(ShippingAddressTable4)
admin.site.register(TestTable)


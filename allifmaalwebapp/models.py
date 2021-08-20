from django.contrib.auth.models import User # this is the default user models
from django.db import models
# create your models here

#the first model is the customer model which contains 3 attributes
class CustomerTable4(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    #onetoone relationship means that a user can only have one customer and customer can have one user
    #on_delete relationship means that delete the item if the user is deleted
    
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
    		return self.name
class ProductTable4(models.Model):
    product_name = models.CharField(max_length=255, null=True)
    product_quantity = models.IntegerField(default=0,null=True,blank=True)
    product_price=models.DecimalField(max_digits=7,decimal_places=2)
    digital = models.BooleanField(default=False,blank=True, null=True)#If the item is digital, we dont need to ship
    #and if digital is false, then it means we need to ship as it is physical item
    #product_image=models.ImageField(null=True, blank=True)
    product_image=models.ImageField(upload_to='static/images/',null=True, blank=True)
       
    def __str__(self):
        return self.product_name
    @property
    def imageOnlineProductURL(self):
        try:
            url=self.product_image.url
        except:
            url=''
        return url
    
class OrderTable4(models.Model):
    customer = models.ForeignKey(CustomerTable4, on_delete=models.SET_NULL, null=True,blank=True)#adding 
    #Customertable here seals the relationship...also on_delete=SET_NULL means that if customer is deleted, the order is not deleted
    #give many_to_one relationship to the customer which means that customer can have multiple orders
    #if customer is deleted, we dont want to delete the order but rather set the customer value to null
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    #if complete is false then that means that is an open cart and we can continue adding more items
    #if true, this is a closed cart
    transaction_id=models.CharField(max_length=100, null=True)#will help to just add extra info to the order
    
    def __str__(self):
        return str(self.id) 
    
#create items that need to be added to our order with the many_to_one relationship using the ForeignKey
#cart can have multiple order items and that is why we need that many_to_one relationship
class OrderItemsTable4(models.Model):#OrderItem is an item within the the cart
    product = models.ForeignKey(ProductTable4, on_delete=models.SET_NULL, null=True, blank=True)# this sets also what product to attach to the order
    order = models.ForeignKey(OrderTable4, on_delete=models.SET_NULL, null=True,blank=True)# order is a cart
    #order is a child of OrderTable model object...a single order can have multiple order items
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)#date added this item to the order
    def __str__(self):
           return self.product
    
class ShippingAddressTable4(models.Model):
     customer = models.ForeignKey(CustomerTable4, on_delete=models.SET_NULL, null=True,blank=True)
     #attach the shipping address to the customer so that if the order gets deleted, you will still have the shipping address for a customer
     order = models.ForeignKey(OrderTable4, on_delete=models.SET_NULL, null=True,blank=True)
     country=models.CharField(max_length=200, null=True)
     physical_address=models.CharField(max_length=200, null=True)
     city=models.CharField(max_length=200, null=True)
     street=models.CharField(max_length=200, null=True)
     mobile=models.CharField(max_length=200, null=True)
     contact_person=models.CharField(max_length=200, null=True)
     date_added = models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
           return self.physical_address

class TestTable(models.Model):
     
     first_name=models.CharField(max_length=200, null=True)
     second_name=models.CharField(max_length=200, null=True)
     
     
     def __str__(self):
           return self.first_name


from django.db import models
import uuid 

class Customer(models.Model):
    customer_id = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    customer_name = models.CharField(max_length=255,blank=True,null=True)
    customer_mobile = models.CharField(max_length=255,blank=True,null=True)
    customer_email = models.CharField(max_length=255,blank=True,null=True)
    customer_username = models.CharField(max_length=255,blank=True,null=True)
    customer_password = models.CharField(max_length=255,blank=True,null=True)
    customer_address = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.customer_name
    

class CargoTypes(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name
    

class Cargo(models.Model):
    cargo_id = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    cargo_customer_id = models.ForeignKey('Customer',on_delete = models.CASCADE)
    cargo_type = models.ForeignKey('CargoTypes',on_delete = models.CASCADE)
    cargo_sales = models.CharField(max_length=255,blank=True,null=True)
    cargo_order = models.CharField(max_length=255,blank=True,null=True)
    cargo_description = models.TextField()

    def __str__(self):
        return f"{self.cargo_type.name} - {self.cargo_id}"
    
class Transaction(models.Model):
    transaction_id = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    transaction_customer_id = models.ForeignKey('Customer',on_delete = models.CASCADE)
    transaction_amount = models.CharField(max_length=255,blank=True,null=True)
    transaction_number = models.CharField(max_length=255,blank=True,null=True)
    transaction_type = models.CharField(max_length=255,blank=True,null=True)
    transaction_descrption = models.TextField()
    transaction_history = models.TextField()

    def __str__(self):
        return f"{self.transaction_customer_id.customer_name} - {self.transaction_amount}"
       

class Billing(models.Model):
    bill_id = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    bill_customer_id = models.ForeignKey('Customer',on_delete = models.CASCADE)
    bill_type = models.CharField(max_length=255,blank=True,null=True)
    bill_receipt = models.CharField(max_length=255,blank=True,null=True)
    bill_description = models.TextField()

    def __str__(self):
        return f"{self.bill_type} - {self.bill_customer_id.customer_name}"
    

class Enquiry(models.Model):
    enquiry_id = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    enquiry_title = models.CharField(max_length=255,blank=True,null=True)
    enquiry_type = models.CharField(max_length=255,blank=True,null=True)
    enquiry_date = models.DateTimeField(auto_now=True)
    enquiry_description = models.TextField()

    def __str__(self):
        return self.enquiry_title

class Payments(models.Model):
    payment_id = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
    payment_customer_id = models.ForeignKey('Customer',on_delete = models.CASCADE)
    payment_date = models.DateTimeField(auto_now=True)
    payment_bill =models.CharField(max_length=255,blank=True,null=True)
    payment_type = models.CharField(max_length=255,blank=True,null=True)
    payment_description = models.TextField()
     
    def __str__(self):
        return f"{self.payment_type} - {self.payment_customer_id.cutomer_name}"
    

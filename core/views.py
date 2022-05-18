from string import capwords
from django.shortcuts import render
from .models import Billing, Cargo, CargoTypes, Customer, Enquiry, Payments, Transaction

def index(request):

    customer = Customer.objects.all().count()
    print(int(customer))
    cargo = Cargo.objects.all().count()
    transaction = Transaction.objects.all().count()
    billing = Billing.objects.all().count()
    payments = Payments.objects.all().count()
    enquiry = Enquiry.objects.all().count()

    data = {
        "customer" : customer,
        "cargo" : cargo,
        "transaction": transaction,
        "billing":billing,
        "payments":payments,
        "enquiry": enquiry
    }

    if request.method == "POST":
        password = request.POST.get("password")
        email = request.POST.get("email")

        if email == "admin@gmail.com" and password == "admin":
            return render(request,"home.html",data)

        else:
            render(request,'index.html')

    return render(request,'index.html')


def addCustomer(request):
    if request.method == "POST":
        customer_name = request.POST.get("customer_name")
        customer_mobile = request.POST.get("customer_mobile")
        customer_email = request.POST.get("customer_email")
        customer_password = request.POST.get("customer_password")
        customer_username = request.POST.get("customer_username")
        customer_address = request.POST.get("customer_address")

        print(customer_address)
        print(customer_email)
        print(customer_mobile)
        print(customer_password)
        print(customer_name)
        print(customer_username)
        try:
            customer = Customer(
                customer_name = customer_name,
                customer_mobile = customer_mobile,
                customer_email = customer_email,
                customer_username = customer_username,
                customer_password = customer_password,
                customer_address = customer_address
            )
            print("Done")
            customer.save()
        
        except:
            print("Failed")
    
    return render(request,"add_customer.html")





def addCargo(request):
    if request.method == "POST":
        cargo_customer_id = request.POST.get("cargo_customer_id")
        cargo_type = request.POST.get("cargo_type")
        cargo_sales = request.POST.get("cargo_sales")
        cargo_order = request.POST.get("cargo_order")
        cargo_description = request.POST.get("cargo_description")

        print(cargo_sales)
        print(cargo_type)
        print(cargo_order)
        print(cargo_customer_id)
        print(cargo_description)
        try:
            cargo = Cargo(
                cargo_customer_id = Customer.objects.filter(customer_id = cargo_customer_id),
                cargo_type = CargoTypes.objects.filter(id=cargo_type),
                cargo_sales = cargo_sales,
                cargo_description = cargo_description,
                cargo_order = cargo_order,
            )
            print("Done")
            cargo.save()
        
        except:
            print("Failed")
    
    return render(request,"add_cargo.html")



def addTransaction(request):
    if request.method == "POST":
        transaction_customer_id = request.POST.get("transaction_customer_id")
        transaction_amount = request.POST.get("transaction_amount")
        transaction_bill = request.POST.get("transaction_bill")
        transaction_number = request.POST.get("transaction_number")
        transaction_type = request.POST.get("transaction_type")
        transaction_history = request.POST.get("transaction_history")
        transaction_description = request.POST.get("transaction_description")
        print(transaction_bill)
        print(transaction_amount)
        print(transaction_number)
        print(transaction_number)
        print(transaction_customer_id)
        print(transaction_type)
        try:
            transaction = transaction(
                transaction_customer_id = Customer.objects.filter(customer_id = transaction_customer_id),
                transaction_bill = transaction_bill,
                transaction_type = transaction_type,
                transaction_number = transaction_number,
                transaction_history = transaction_history,
                transaction_description = transaction_description,
            )
            print("Done")
            transaction.save()
        
        except:
            print("Failed")
    
    return render(request,"add_transaction.html")
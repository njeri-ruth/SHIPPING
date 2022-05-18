from django.contrib import admin

admin.site.site_header = 'SHIPPING'
admin.site.site_title = 'SHIPPING'

from .models import (Customer,Cargo,Billing,Transaction,Enquiry,Payments,CargoTypes)

admin.site.register(Customer)
admin.site.register(Cargo)
admin.site.register(Billing)
admin.site.register(Transaction)
admin.site.register(Enquiry)
admin.site.register(Payments)
admin.site.register(CargoTypes)

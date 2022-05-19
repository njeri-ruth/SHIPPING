
from django.urls import path
from .views import index,addCustomer,home

app_name = "core"

urlpatterns = [
    path('',index,name='Login'),
    path('add_customer/',addCustomer,name='add-customer'),
    path("home/",home,name="home")
]

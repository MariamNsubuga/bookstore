from django.contrib import admin
from .models import Customer, Book, Order, Request_Book
# Register your models here.
admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(Request_Book)

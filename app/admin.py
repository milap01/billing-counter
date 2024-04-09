from django.contrib import admin
from .models import Customer,Employee,Product,Bill

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Bill)
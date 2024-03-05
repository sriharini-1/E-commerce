from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Account_details)
admin.site.register(Products)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Order_items)
admin.site.register(Accessories)


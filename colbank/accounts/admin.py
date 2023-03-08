from django.contrib import admin
from . models import Account, Customer, Transfer ,  Widthrawal, Deposit

# Register your models here.


admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Transfer)
admin.site.register(Widthrawal)
admin.site.register(Deposit)
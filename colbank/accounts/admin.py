from django.contrib import admin
from . models import Account, Customer, Transfer ,  Withdrawal, Deposit

# Register your models here.


admin.site.register(Account)
admin.site.register(Customer)
admin.site.register(Transfer)
admin.site.register(Withdrawal)
admin.site.register(Deposit)
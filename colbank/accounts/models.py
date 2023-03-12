from django.db import models
from django.contrib.auth.models import User

import random
# Create your models here.

# This model includes three fields: 'account_number', 'balance', and 'customer'.
# 'account_number' is a unique string that identifies the account
# 'balance' is a decimal number representing the account balance, and 'customer'
# is a foreign key relationship to the 'customer' model, indicating which customer owns the account.
def random_string():
    return str(random.randint(10000, 99999))

class Account(models.Model):
    account_number = models.CharField(default=random_string, unique=True, max_length=10)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

    def __str__(self):
        return self.account_number

class Customer(models.Model):
     # Fields
     user_name = models.CharField(max_length=32, help_text='Enter  username')
     user_email = models.EmailField(max_length=254, help_text='Enter email address')
     user = models.OneToOneField(User,on_delete=models.CASCADE)


class Transfer(models.Model):
    sender_id = models.ForeignKey("Account", on_delete=models.CASCADE, related_name='Transfer')
    receiver_id = models.ForeignKey("Account", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference =models.CharField(max_length=20)
    date_created = models.DateField(auto_now_add=True)


class Withdrawal(models.Model):

     account_id = models.ForeignKey('Account', on_delete=models.CASCADE, null=True)
     amount = models.DecimalField(max_digits=8,decimal_places=2)
     reference =models.CharField(max_length=20)
     date_created = models.DateField(auto_now_add=True)
     
class Deposit(models.Model):
    account_id = models.ForeignKey("Account", on_delete=models.CASCADE)
    amount = models.DecimalField( max_digits=10, decimal_places=2)
    reference =models.CharField(max_length=20)
    date_created = models.DateField( auto_now_add=True)
    

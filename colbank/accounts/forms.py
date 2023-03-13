from django import forms
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Deposit, Withdrawal, Transfer,Customer,Account


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields= ('account_id','amount','reference')


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields= ('account_id','amount','reference')


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields= ('customer','account_number')

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields= ('sender_id','receiver_id','amount','reference')



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    model = Customer
    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
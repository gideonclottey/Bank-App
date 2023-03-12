from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .models import Account, Transfer, Withdrawal, Deposit, Customer
from .forms import DepositForm
from django.db.models import Sum
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name ='accounts/signup.html'
    success_url ='/dashboard/'


class LoginInterfaceView(LoginView):
    template_name = 'accounts/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'
    



def home(request):
    return render(request, 'home_list.html', {})

    

def dash_board(request):
    return render(request, 'dashboard.html',{})

class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    success_url ='/dashboard/'

class WithdrawalCreateView(CreateView):
    model = Withdrawal
    form_class = DepositForm
    success_url ='/dashboard/'

class TransferCreateView(CreateView):
    model = Transfer
    form_class = DepositForm
    success_url ='/dashboard/'
    
    

def about(request):
    return render(request, 'about.html',{})



class CustomerTransactionView(TemplateView):
    template_name = 'customer_transaction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customers = Customer.objects.all()
        transactions = []
        for customer in customers:
            customer_accounts = Account.objects.filter(customer=customer)
            for account in customer_accounts:
                account_transactions = []
                account_balance = account.balance
                deposits = Deposit.objects.filter(account_id=account)
                for deposit in deposits:
                    account_balance += deposit.amount
                    account_transactions.append({
                        'type': 'Deposit',
                        'amount': deposit.amount,
                        'reference': deposit.reference,
                        'date_created': deposit.date_created,
                        'balance': account_balance
                    })
                withdrawals = Withdrawal.objects.filter(account_id=account)
                for withdrawal in withdrawals:
                    account_balance -= withdrawal.amount
                    print(account_balance)
                    account_transactions.append({
                        'type': 'Withdrawal',
                        'amount': withdrawal.amount,
                        'reference': withdrawal.reference,
                        'date_created': withdrawal.date_created,
                        'balance': account_balance
                    })
                transfers = Transfer.objects.filter(sender_id=account)
                for transfer in transfers:
                    account_balance -= transfer.amount
                    account_transactions.append({
                        'type': 'Transfer',
                        'amount': transfer.amount,
                        'reference': transfer.reference,
                        'date_created': transfer.date_created,
                        'balance': account_balance
                    })
                transactions.extend(account_transactions)
        context['transactions'] = transactions
        return context
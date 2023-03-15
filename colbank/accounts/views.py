from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.views.generic import CreateView, TemplateView
from .models import Account, Transfer, Withdrawal, Deposit, Customer
from .forms import DepositForm,NewUserForm,WithdrawalForm,TransferForm,AccountForm
from django.db.models import Sum
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("account.create")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dash-board")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="accounts/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("home.list")


class AccountCreation(CreateView):
    model = Account
    form_class = AccountForm
    success_url ='/dashboard/'
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
    form_class = WithdrawalForm
    success_url ='/dashboard/'

class TransferCreateView(CreateView):
    model = Transfer
    form_class = TransferForm
    success_url ='/dashboard/'
    
    

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})

class CustomerTransactionView(TemplateView):
    template_name = 'dashboard.html'

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
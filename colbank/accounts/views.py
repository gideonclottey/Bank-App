from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from . models import Deposit
from .forms import DepositForm

# Create your views here.


def home(request):
    return render(request, 'home_list.html', {})

def login_view(request):
    if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('dash_board')
         else:
            messages.error(request, 'Invalid username or password') 
    return render(request, 'login.html')

def dash_board(request):
    return render(request, 'dashboard.html',{})

class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    

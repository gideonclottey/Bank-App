from django.shortcuts import render
from django.views.generic import CreateView
from . models import Deposit
from .forms import DepositForm

# Create your views here.


def home(request):
    return render(request, 'home_list.html', {})






def contact_us(request):
    return render(request, 'contact_us.html', {})


def dash_board(request):
    return render(request, 'dashboard.html',{})

class DepositCreateView(CreateView):
    model = Deposit
    form_class = DepositForm
    success_url ='/dashboard/'
    

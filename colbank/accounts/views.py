from django.shortcuts import render
from django.views.generic import CreateView
from . models import Deposit

# Create your views here.


def home(request):
    return render(request, 'home_list.html', {})

class DepositCreateView(CreateView):
    model = Deposit

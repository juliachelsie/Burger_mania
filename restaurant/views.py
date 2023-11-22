from django.shortcuts import render
from django.views import generic
from .models import Reservation
from django.shortcuts import render
from .forms import Reserve_table_form
from django.http import HttpResponseRedirect


# Create your views here.
def get_index(request):
    return render(request, 'restaurant/index.html')


def get_menu(request):
    return render(request, 'restaurant/menu.html')


def get_base(request):
    return render(request, 'restaurant/base.html')


def get_book(request):
    context = {}
    form = Reserve_table_form()
    context['form'] = form
    return render(request, 'restaurant/book.html', context)

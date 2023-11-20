from django.shortcuts import render
from django.views import generic
from .models import Reservation
from django.shortcuts import render
from .forms import Reserve_table_form


# Create your views here.

def reserve_table(request):

    context = {}

    return render(request, 'restaurant/book.html', context)


def get_index(request):
    return render(request, 'restaurant/index.html')


def get_menu(request):
    return render(request, 'restaurant/menu.html')


def get_base(request):
    return render(request, 'restaurant/base.html')


def get_book(request):
    return render(request, 'restaurant/book.html')

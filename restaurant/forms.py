from django import forms
from .models import Reservation


class Reserve_table_form(forms.Form):
    model = Reservation
    Name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'style': 'width: 300px;', 'class': 'form-control'}))
    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}))
    reserve_phone = forms.IntegerField(widget=forms.TextInput(
        attrs={'placeholder': 'Phone-number', 'style': 'width: 300px;', 'class': 'form-control'}))
    number_of_people = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Number of people', 'style': 'width: 300px;', 'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date', 'style': 'width: 300px;'}))
    time = forms.TimeField(widget=forms.TimeInput(
        attrs={'style': 'width: 300px;', 'class': 'form-control', 'type': 'time'}))

from django import forms
from .models import Reservation


class Reserve_table_form(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

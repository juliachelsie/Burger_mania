from django import forms
from .models import Reservation


class Reserve_table_form(forms.Form):
    model = Reservation
    reserve_name = forms.CharField(label='Your Name')
    reserve_email = forms.EmailField(label='Your Email')
    reserve_phone = forms.IntegerField(label='Your Phone-number')
    reserve_people = forms.IntegerField(label='How many are you')
    reserve_date = forms.DateField(label='When do you want to visit?')
    reserve_time = forms.TimeField(label='What time do you want to visit?')

    # class Reserve_table_form(forms.ModelForm):
    # class Meta:
    # model = Reservation
    # fields = ["name", "email", "phone_number",
    # "number_of_people", "date", "time",]

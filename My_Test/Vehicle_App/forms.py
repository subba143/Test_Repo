from django import forms
class VehicleForm(forms.Form):
    vin = forms.CharField(max_length=17)
    make = forms.CharField(max_length=100)
    model = forms.CharField(max_length=100)
    year = forms.IntegerField()
    color = forms.CharField(max_length=20)
    mileage = forms.FloatField()
    v_type = forms.CharField(max_length=50)
    seats = forms.IntegerField()
    v_seat_type = forms.CharField(max_length=50)
    owner = forms.CharField(max_length=100)
    o_contact = forms.IntegerField()
    feedback = forms.CharField()

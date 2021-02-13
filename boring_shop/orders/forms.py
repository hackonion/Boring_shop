from django import forms
from django.forms import fields
from .models import Order

class OrderCreatedForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['firt_name','last_name','email','address',
                  'postal_code','city']
        
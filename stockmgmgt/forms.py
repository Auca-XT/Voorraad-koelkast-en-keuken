from django import forms
from .models import Stock

class stockCreateForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['category', 'item_name', 'quantity']
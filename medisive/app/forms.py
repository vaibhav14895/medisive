from models import Costumer
from django import forms
class CostumerForm(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = ['name', 'email', 'phone', 'message']
       
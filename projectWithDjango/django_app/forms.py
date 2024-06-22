from django import forms
from .models import fruitVariety

class FruitVarietyForm(forms.Form) :

    fruit_variety = forms.ModelChoiceField(queryset=fruitVariety.objects.all(), label="Select Fruit Variety!")     # it will make the drop down
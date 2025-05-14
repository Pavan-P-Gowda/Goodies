from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' :'form-class','placeholder': 'Enter car name'}),
            'price' : forms.NumberInput(attrs={'class': 'form-class','placeholder': 'Enter car price'}),
            'img' : forms.ClearableFileInput(attrs={'class':'form-class'}),
        }
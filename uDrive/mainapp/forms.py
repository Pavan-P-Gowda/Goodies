from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class' :'form-class col-sm-9','placeholder': 'Enter car name'}),
            'price' : forms.NumberInput(attrs={'class': 'form-class col-sm-9','placeholder': 'Enter car price'}),
            'img' : forms.ClearableFileInput(attrs={'class':'form-class col-sm-9'}),
            # 'fuel' : forms.ChoiceField(
            #     choices = Car._meta.get_field('fuel').choices,
            #     widget = forms.Select(attrs={'class':'form.class'}),
            #     initial='petrol'
            # )
            'fuel' : forms.Select(attrs={'class':'form-class col-sm-9'}),
            'transmission' : forms.TextInput(attrs={'class': 'form-class col-sm-9'}),
            'seat':forms.TextInput(attrs={'class':'form-class col-sm-9'}),
            'year': forms.NumberInput(attrs={'class': 'form-class col-sm-9'}),
            'desc' : forms.TextInput(attrs={'class' :'form-class col-sm-9','placeholder': 'About car'}),
            'caption' : forms.TextInput(attrs={'class' :'form-class col-sm-9','placeholder': ' Enter Caption'})
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['img','price','fuel','transmission']
        widgets = {
            'img' : forms.FileInput(attrs={'class':'form-class col-sm-15'}),
            'price' : forms.NumberInput(attrs={'class': 'form-class col-sm-9','placeholder': 'Enter car price'}),
            'fuel' : forms.Select(attrs={'class':'form-class col-sm-9'}),
            'transmission' : forms.TextInput(attrs={'class': 'form-class col-sm-9'}),

        }
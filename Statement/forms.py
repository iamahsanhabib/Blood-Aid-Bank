from django.forms import ModelForm, TextInput,Select, FileInput,NumberInput, DateInput
from Statement.models import Tax, Financial, BloodDonation, DailyDonation, TotalDonation
from django import forms

class TaxForm(ModelForm):
    class Meta:
        model = Tax
        fields ='__all__'
        widgets = {
            'name': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'category': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'amount': NumberInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'month': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'date' : DateInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
        }

class FinancialForm(ModelForm):
    class Meta:
        model = Financial
        fields ='__all__'
        widgets = {
            'name': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'des': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'category': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'amount': NumberInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'month': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'date' : DateInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
        }

class BloodDonationForm(ModelForm):
    class Meta:
        model = BloodDonation
        fields ='__all__'
        widgets = {
            'name1': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'phone1': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'blood_group': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'name2': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'problem': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'phone2': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'date' : DateInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'location': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'bag': NumberInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'ref_name': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
        }

class DailyDonationForm(ModelForm):
    class Meta:
        model = DailyDonation
        fields ='__all__'
        widgets ={
            'bag': NumberInput(attrs={'class': 'form-control'}),
        }

class TotalDonationForm(ModelForm):
    class Meta:
        model = TotalDonation
        fields ='__all__'
        widgets ={
            'bag': NumberInput(attrs={'class': 'form-control'})
        }
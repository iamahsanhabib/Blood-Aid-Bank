from django.forms import ModelForm, TextInput,Select, FileInput, DateInput,NumberInput
from Bloodbank.models import Applicant, Donor, Booking, OrganizationMember, BloodGroup
from django import forms

class BloodGroupForm(ModelForm):
    class Meta:
        model = BloodGroup
        fields = '__all__'

class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        fields ='__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'phone': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'institution': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'blood_group': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'location': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'zilla': Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'image': FileInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'ref_name': TextInput(attrs={'class': 'form-control mt-1 mb-2 border-warning','placeholder':'সংগঠনে পরিচিত ব্যক্তি'}),
        }

class DonorForm(ModelForm):
    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'date':DateInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
            'number_donation': NumberInput(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
        }

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'statement':Select(attrs={'class': 'form-control mt-1 mb-2 border-warning'}),
        }

class OrganizationMemberForm(ModelForm):
    class Meta:
        model = OrganizationMember
        fields = '__all__'

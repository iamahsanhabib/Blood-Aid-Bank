from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from Bloodbank.forms import DonorForm, BloodGroupForm, OrganizationMemberForm
from Bloodbank.models import Donor, OrganizationMember
import datetime, random
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

def addDonor(request):
    form = DonorForm()
    changed = False
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            changed = True
    diction = {
        'changed':changed,
        'form': form,
    }
    return render(request, 'Bloodbank/add_donor.html', context=diction)
def showDonor(request):
    donor = Donor.objects.order_by('blood_group','date').all()
    form = BloodGroupForm()
    diction ={
        'list': donor,
        'form': form,
    }
    return render(request, 'Bloodbank/donor.html', context=diction)
def searchDonor(request):
    form = BloodGroupForm()
    '''if request.method == 'POST':
        form = BloodGroupForm(request.POST)
        group = request.POST.get('blood_group')
        donor = Donor.objects.filter(Q(blood_group=group)).order_by('blood_group','date')
        if(len(donor)==0):
            donor = Donor.objects.order_by('blood_group','date').all()
        diction ={
            'list': donor,
            'group': group,
            'form': form,
        }'''
    diction = {
        'form': form,
    }
    return render(request, 'Bloodbank/donor.html', context=diction)

def show_Donor(request):
    donor = Donor.objects.order_by('blood_group','date').all()
    form = BloodGroupForm()
    return render(request, 'Bloodbank/blood_donor_list.html', context={'donor':donor, 'form':form})

@login_required
def show_Donor_Details(request, pk):
    donor = Donor.objects.get(id=pk)
    return render(request, 'Bloodbank/details_blood_donor.html', context={'donor':donor})

@login_required
def update_Donor_Details(request,pk):
    donor = Donor.objects.get(id=pk)
    form  = DonorForm(instance=donor)
    if request.method == 'POST':
        form = DonorForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('/donor/')
    return render(request, 'Bloodbank/update_blood_donor.html', context={'form': form})

def search_donor(request):
    if request.method == 'POST':
        blood_group = request.POST.get('blood_group')
        donor = Donor.objects.order_by('blood_group','date').filter(blood_group=blood_group)
        check = False
        if blood_group == 'Choose...':
            donor = Donor.objects.order_by('blood_group','date').all()
        if not donor and  blood_group != 'Choose...':
            check = True
            donor = Donor.objects.order_by('blood_group','date').all()
        return render(request, 'Bloodbank/blood_donor_list.html', context={'donor':donor,'check':check})

@login_required
def delete_donor(request,pk):
    donor = Donor.objects.get(pk=pk)
    if request.method == 'POST':
        donor.delete()
        return redirect('/donor/')
    return render(request, 'Bloodbank/delete_donor.html')

def showMember(request):
    member = OrganizationMember.objects.order_by('name').all()
    diction = {
        'member':member,
    }
    return render(request, 'Bloodbank/member.html', context=diction)

def detailsMember(request, pk):
    member =OrganizationMember.objects.get(id=pk)
    diction = {
        'member':member,
    }
    return render(request, 'Bloodbank/member_details.html', context=diction)

@login_required
def add_member(request):
    form = OrganizationMemberForm()
    if request.method == 'POST':
        form = OrganizationMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/Member/')
    return render(request, 'Bloodbank/add_Organization_Member.html', context={'form': form})

@login_required
def update_member_profile(request,pk):
    member = OrganizationMember.objects.get(id=pk)
    form = OrganizationMemberForm(instance= member)
    if request.method == 'POST':
        form = OrganizationMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('/Member/')
    return render(request, 'Bloodbank/update_member_profile.html', context={'form': form})
    



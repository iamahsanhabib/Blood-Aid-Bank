from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from Bloodbank.forms import DonorForm, BloodGroupForm, OrganizationMemberForm, ApplicantForm, BookingForm
from Bloodbank.models import Donor, OrganizationMember, Applicant, Booking, About
from Statement.models import DailyDonation, TotalDonation, DonationPhoto
import datetime, random
from django.db.models import Q, Sum
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    daily = DailyDonation.objects.all().last()
    total = TotalDonation.objects.all().last()
    photo = DonationPhoto.objects.all().last()
    donation = Donor.objects.order_by('-number_donation')[0:5]
    context ={
        'daily':daily,
        'total':total,
        'donation':donation,
        'photo':photo
    }
    return render(request, 'index.html', context=context)

def addDonor(request):
    changed = False
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        institution = request.POST.get('institution')
        blood_group = request.POST.get('blood')
        date = request.POST.get('date')
        location = request.POST.get('upozila')
        zilla = request.POST.get('zilla')
        mydata = Donor(name=name, phone=phone,institution=institution, blood_group=blood_group, date=date, location=location, zilla=zilla)
        mydata.save()
        changed = True
    diction = {
        'changed':changed,
    }
    return render(request, 'Bloodbank/add_donor.html', context=diction)

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
    form = BloodGroupForm()
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
    
def addMember(request):
    form = ApplicantForm()
    changed = False
    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            changed = True
            #return render(request, 'bloodaidbank/form.html')
    diction={
        'form': form,
        'changed': changed,
    }
    return render(request, 'Bloodbank/add_member.html', context=diction)

@login_required
def show_application_list(request):
    list = Applicant.objects.order_by('-id').all()
    #print(list)
    return render(request, 'Bloodbank/member_application_list.html', context={'list': list})
@login_required
def show_application_details(request,pk):
    list = Applicant.objects.get(pk=pk)
    return render(request, 'Bloodbank/member_application_details.html', context={'list':list})

@login_required
def delete_application_list(request,pk):
    application = Applicant.objects.get(pk=pk)
    print(application)
    if request.method == 'POST':
        application.delete()
        return redirect('/Application/List/')
    return render(request, 'Bloodbank/application_list_delete.html')


def bookBlood(request):
    changed = False
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            changed = True
        
    diction = {
        'changed':changed,
        'form':form,
    }
    return render(request, 'Bloodbank/booking.html', context=diction)

def show_booking_list(request):
    booking = Booking.objects.order_by('-month').all()
    return render(request, 'Bloodbank/booking_list.html', context={'booking':booking})

def show_booking_details(request, pk):
    booking = Booking.objects.get(id=pk)
    form  = BookingForm(instance=booking)
    changed = False
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            changed = True
    context={
        'booking':booking,
        'form':form,
        'changed':changed,
    }
    return render(request, 'Bloodbank/booking_list_detail.html', context=context)

@login_required
def delete_booking(request,pk):
    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('/Blood_Booking/list')
    return render(request, 'Bloodbank/delete_booking_list.html')

def showAbout(request):

    about = About.objects.all().last()
    diction = {
        'about':about,
    }
    return render(request, 'Bloodbank/about.html', context=diction)
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Statement.models import Tax, Financial, BloodDonation, DailyDonation, TotalDonation
from Statement.forms import TaxForm, FinancialForm, BloodDonationForm, DailyDonationForm, TotalDonationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.db.models import Sum,Q

# Create your views here.
#Tax Block
@login_required
def addTax(request):
    form = TaxForm()
    changed = False
    if request.method =='POST':
        form =TaxForm(request.POST)
        if form.is_valid():
            form.save()
            changed = True
            return redirect('/statement/tax/')
    return render(request, 'Statement/add_tax.html', context={'form':form, 'changed':changed})
@login_required
def showTax(request):
    tax = Tax.objects.order_by('-date').all()
    amount = Tax.objects.aggregate(Sum('amount'))
    return render(request, 'Statement/tax.html',context={'tax':tax,'amount':amount})

@login_required
def deleteTax(request, pk):
    tax = Tax.objects.get(pk=pk)
    if request.method =='POST':
        tax.delete()
        return redirect('/statement/tax/')
    context={
        'tax': tax,
    }
    return render(request, 'Statement/delete_tax.html',context={'tax':tax})

#Financial Block -
@login_required
def addFinancial(request):
    form = FinancialForm()
    if request.method == 'POST':
        form = FinancialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/statement/financial/')
    return render(request, 'Statement/add_financial.html',context={'form':form})

@login_required
def show_financial(request):
    financial = Financial.objects.order_by('-date').all()
    amount1 = Financial.objects.filter(Q(category='খরচ')).aggregate(Sum('amount'))
    amount2 = Financial.objects.filter(Q(category='জমা')).aggregate(Sum('amount'))
    x,y = 0,0
    if amount1['amount__sum'] is not None:
        x = amount1['amount__sum']
    if amount2['amount__sum'] is not None:
        y = amount2['amount__sum']
    context={
        'financial': financial,
        'x': x,
        'y': y,
        'amount3': y-x
    }
    return render(request, 'Statement/financial.html', context=context)

@login_required
def delete_financial(request, pk):
    financial = Financial.objects.get(pk=pk)
    if request.method =='POST':
        financial.delete()
        return redirect('/statement/financial/')
    context={
        'financial': financial,
    }
    return render(request, 'Statement/delete_financial.html',context={'financial':financial})

#Blood Donation statement
@login_required
def show_blood_statment(request):
    blood_donation = BloodDonation.objects.order_by('-date').all()
    return render(request, 'Statement/blood_statement.html', context={'blood_donation':blood_donation})

@login_required
def add_blood_statment(request):
    form = BloodDonationForm()
    if request.method == 'POST':
        form = BloodDonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/statement/blood-donation/')
    return render(request, 'Statement/add_blood_statement.html', {'form': form})

@login_required
def delete_blood_statment(request, pk):
    blood_donation = BloodDonation.objects.get(pk=pk)
    if request.method =='POST':
        blood_donation.delete()
        return redirect('/statement/blood-donation/')
    context={
        'blood_donation': blood_donation
    }
    return render(request, 'Statement/delete_blood_statement.html',context={'blood_donation':blood_donation})

@login_required
def show_blood_donation(request):
    daily = DailyDonation.objects.latest('date')
    context ={
        'daily':daily,
    }
    return render(request, 'Statement/show_blood_donation', context=context)
@login_required
def add_blood_donation(request):
    daily = DailyDonation.objects.all().last()
    form1 = DailyDonationForm(instance = daily)
    if request.method =='POST':
        form1 = DailyDonationForm( request.POST)
        if form1.is_valid():
            form1 = DailyDonationForm( request.POST,instance = daily)
            form1.save()
            daily = DailyDonation.objects.all().last()
            form1 = DailyDonationForm(instance = daily)
            return redirect('/')
    context ={
        'form1': form1,
        'daily':daily,
    }
    return render(request, 'Statement/daily_blood_donation.html', context=context)
@login_required
def total_blood_donation(request):
    total = TotalDonation.objects.all().last()
    form2 = TotalDonationForm(instance = total)
    if request.method =='POST':
        form2 = TotalDonationForm( request.POST)
        if form2.is_valid():
            form2 = TotalDonationForm( request.POST,instance = total)
            form2.save()
            total = TotalDonation.objects.all().last()
            form2 = TotalDonationForm(instance = total)
            return redirect('/')
    context ={
        'form2': form2,
        'total': total
    }
    return render(request, 'Statement/total_blood_donation.html', context=context)
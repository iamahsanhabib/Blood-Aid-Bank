from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.aggregates import Count
from random import randint

class Zilla(models.Model):
    zilla = models.CharField(max_length=100, blank=False, null=False, verbose_name="জেলা")
    def __str__(self):
        return self.zilla
    class Meta:
        verbose_name_plural = "Zilla"

class Upazila(models.Model):
    upazila = models.CharField(max_length=100, blank=False, null=False, verbose_name="উপজেলা/থানা")

    def __str__(self):
        return self.upazila
    class Meta:
        verbose_name_plural = "Upazilla"

class BloodGroup(models.Model):
    group = models.CharField(max_length=6, blank=False, null=False, verbose_name="রক্তের গ্রুপ")
    def __str__(self):
        return self.group
    class Meta:
        verbose_name_plural = "Blood Group"

class Applicant(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'সদস্য নাম')
    phone = models.CharField(max_length = 14, verbose_name = 'মোবাইল নাম্বার')
    institution = models.CharField(max_length = 100, verbose_name = 'শিক্ষা-প্রতিষ্ঠান')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, verbose_name = 'রক্তের গ্রুপ', null=False)
    location = models.ForeignKey(Upazila, on_delete=models.CASCADE, verbose_name="উপজেলা/থানা", null=False)
    zilla = models.ForeignKey(Zilla, on_delete=models.CASCADE, verbose_name="জেলা", null=False)
    ref_name = models.CharField(max_length = 100, verbose_name = 'রেফারেন্স')
    image  = models.ImageField(upload_to = 'Applicant/', default = '', verbose_name = 'ছবি')
    REQUIRED_FIELDS = ('name', 'phone','institution', 'blood_group','location','zilla','ref_name','image')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Applicant"

class Designation(models.Model):
    designation = models.CharField(max_length = 200, verbose_name ="পদবি")
    def __str__(self):
        return self.designation
    class Meta:
        verbose_name_plural = "Designation"

class Donor(models.Model):
    BLOOD_GROUP_CHOICE = (
        ('A+', 'A+'),
        ('B+', 'B+'),
        ('O+', 'O+'),
        ('AB+', 'AB+'),
        ('A-', 'A-'),
        ('B-', 'B-'),
        ('O-', 'O-'),
        ('AB-', 'AB-'),
    )
    name = models.CharField(max_length = 100, verbose_name = 'রক্তদাতা নাম')
    phone = models.CharField(max_length = 14, verbose_name = 'মোবাইল নাম্বার')
    institution = models.CharField(max_length = 100, verbose_name = 'শিক্ষা-প্রতিষ্ঠান')
    blood_group = models.CharField(max_length = 6,default = 'Select', choices = BLOOD_GROUP_CHOICE, verbose_name = 'রক্তের গ্রুপ', null=False)
    number_donation = models.IntegerField(default=0, verbose_name ="মোট রক্তদান")
    date = models.DateField(auto_now_add=False,verbose_name = 'রক্তদানের-তারিখ', default=datetime.datetime.now)
    location = models.CharField(max_length = 100, verbose_name = 'উপজেলা')
    zilla = models.CharField(max_length = 100, verbose_name = 'জেলা')
    REQUIRED_FIELDS = ('name', 'phone','institution', 'blood_group','date','location','zilla')

    def __str__(self):
        return self.name + ' | ' + self.blood_group
    class Meta:
        ordering = ['blood_group']
        verbose_name_plural = "Donor"
        
class OrganizationMember(models.Model):
    GENDER_CHOICE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    id_no = models.CharField(max_length =15, null = True, blank = True, verbose_name ="আইডি নং-")
    name = models.CharField(max_length=100, verbose_name="সদস্যের নাম")
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE, max_length=200, verbose_name = 'পদবি', null=False)
    gender = models.CharField(max_length = 10,default = 'Select', choices = GENDER_CHOICE, verbose_name = 'লিঙ্গ', null=False)
    phone = models.CharField(max_length =14, verbose_name="মোবাইল নাম্বার")
    institution = models.CharField(max_length = 100, verbose_name = 'শিক্ষা-প্রতিষ্ঠান')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, verbose_name = 'রক্তের গ্রুপ', null=False)
    location = models.ForeignKey(Upazila, on_delete=models.CASCADE, verbose_name="উপজেলা/থানা", null=False)
    zilla = models.ForeignKey(Zilla, on_delete=models.CASCADE, verbose_name="জেলা", null=False)
    image  = models.ImageField(upload_to = 'Member/', default = '', verbose_name = 'ছবি')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Member"
class Month(models.Model):
    month = models.CharField(max_length =20, blank=False, null=False, verbose_name="মাস")
    def __str__(self):
        return self.month
    class Meta:
        verbose_name_plural = "Month"

class Booking(models.Model):
    STATEMENT =(
        ('সংগ্রহ চলছে','সংগ্রহ চলছে'),
        ('যোগাযোগ করুন','যোগাযোগ করুন'),
    )
    WEEK = (
        ('১ম', '১ম'),
        ('২য়', '২য়'),
        ('৩য়', '৩য়'),
        ('৪র্থ', '৪র্থ'),
    )
    name = models.CharField(max_length = 100, verbose_name = 'রক্তদাতা নাম')
    phone = models.CharField(max_length = 14, verbose_name = 'মোবাইল নাম্বার')
    problem = models.CharField(max_length = 100, verbose_name = 'রোগীর সমস্যা')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, verbose_name = 'রক্তের গ্রুপ', null=False)
    month = models.ForeignKey(Month, on_delete=models.CASCADE, verbose_name = 'মাস',)
    week = models.CharField(max_length = 100, verbose_name = 'সপ্তাহ', choices=WEEK)
    location = models.ForeignKey(Upazila, on_delete=models.CASCADE, verbose_name="উপজেলা/থানা", null=False)
    zilla = models.ForeignKey(Zilla, on_delete=models.CASCADE, verbose_name="জেলা", null=False)
    statement = models.CharField(max_length = 100, verbose_name = 'রক্তের অবস্থা', choices=STATEMENT, blank = True, null = False)
    REQUIRED_FIELDS = ('name', 'phone','problem', 'blood_group','month','week', 'location','zilla')

    def __str__(self):
        return self.blood_group
    class Meta:
        verbose_name_plural = "Blood Booking"

class About(models.Model):
    description1 = models.TextField(verbose_name="বিস্তারিত-১")
    description2 = models.TextField(verbose_name="বিস্তারিত-২")
    description3 = models.TextField(verbose_name="বিস্তারিত-৩")
    chairman_img = models.ImageField(upload_to='chairman/', default = '', verbose_name = 'ছবি')

    def __str__(self):
        return 'About BABJ'
    class Meta:
        verbose_name_plural = "About BABJ"
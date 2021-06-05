from django.db import models
from Bloodbank.models import OrganizationMember
import datetime

# Create your models here.
class Tax(models.Model):
    TAX_CHOICES =(
        ('চাঁদা','চাঁদা'),
        ('অনুদান','অনুদান'),
        ('অনান্য','অনান্য'),
    )
    MONTH_CHOICES = (
        ('জানুয়ারি', 'জানুয়ারি'),
        ('ফেব্রুয়ারি', 'ফেব্রুয়ারি'),
        ('মার্চ', 'মার্চ'),
        ('এপ্রিল','এপ্রিল'),
        ('মে', 'মে'),
        ('জুন', 'জুন'),
        ('জুলাই', 'জুলাই'),
        ('আগস্ট', 'আগস্ট'),
        ('সেপ্টেম্বর', 'সেপ্টেম্বর'),
        ('অক্টোবর', 'অক্টোবর'),
        ('নভেম্বর', 'নভেম্বর'),
        ('ডিসেম্বর', 'ডিসেম্বর'),
    )
    name = models.ForeignKey(OrganizationMember, on_delete=models.CASCADE, verbose_name="নাম")
    category = models.CharField(max_length =100, default="চাঁদা", choices=TAX_CHOICES, verbose_name="বিবরণী", null=False)
    amount = models.IntegerField(null=False, default=0, verbose_name="পরিমাণ")
    month = models.CharField(max_length= 100, choices=MONTH_CHOICES, verbose_name="মাস")
    date = models.DateField(auto_now_add=True, verbose_name="তারিখ")

    REQUIRED_FIELDS = ('name', 'category','amount', 'month')

    def __str__(self):
        return self.name

class Financial(models.Model):
    DES_CHOICES = (
        ('জমা','জমা'),
        ('খরচ','খরচ'),
        
    )
    MONTH_CHOICES = (
        ('জানুয়ারি', 'জানুয়ারি'),
        ('ফেব্রুয়ারি', 'ফেব্রুয়ারি'),
        ('মার্চ', 'মার্চ'),
        ('এপ্রিল','এপ্রিল'),
        ('মে', 'মে'),
        ('জুন', 'জুন'),
        ('জুলাই', 'জুলাই'),
        ('আগস্ট', 'আগস্ট'),
        ('সেপ্টেম্বর', 'সেপ্টেম্বর'),
        ('অক্টোবর', 'অক্টোবর'),
        ('নভেম্বর', 'নভেম্বর'),
        ('ডিসেম্বর', 'ডিসেম্বর'),
    )
    date = models.DateField(auto_now_add=True)
    name = models.ForeignKey(OrganizationMember, on_delete=models.CASCADE, verbose_name="নাম")
    des = models.CharField(max_length = 100, verbose_name = 'বিবরণী')
    category = models.CharField(max_length =100, choices = DES_CHOICES, verbose_name ="ক্যাটেগরি")
    amount = models.IntegerField(default=0, verbose_name ="পরিমাণ")
    month = models.CharField(max_length= 100, choices=MONTH_CHOICES, verbose_name="মাস")

    REQUIRED_FIELDS = ('name', 'des', 'amount', 'category','month')

    def __str__(self):
        return self.category

class BloodDonation(models.Model):
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
    name1 = models.CharField(max_length = 100, verbose_name = 'রক্তদাতা নাম')
    phone1 = models.CharField(max_length = 14, verbose_name = 'রক্তদাতার নাম্বার')
    blood_group = models.CharField(max_length = 6,default = 'Select', choices = BLOOD_GROUP_CHOICE, verbose_name = 'রক্তের গ্রুপ', null=False)
    name2 = models.CharField(max_length = 100, verbose_name = 'রোগীর নাম')
    problem = models.CharField(max_length = 14, verbose_name = 'রোগীর সমস্যা')
    phone2 = models.CharField(max_length = 14, verbose_name = 'রোগীর নাম্বার')
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length = 100, verbose_name = 'রক্তদানের স্থান')
    bag = models.IntegerField(default=1, verbose_name = 'রক্তের পরিমাণ')
    ref_name = models.ForeignKey(OrganizationMember, on_delete=models.CASCADE, verbose_name="রেফারেন্স")
    def __str__(self):
        return self.name1 + ' - ' + self.name2

class DailyDonation(models.Model):
    date = models.DateField(auto_now_add=True)
    bag = models.IntegerField(default=0, verbose_name ="পরিমাণ")

    def __str__(self):
        return str(self.bag) + ' | ' + str(self.date)

class TotalDonation(models.Model):
    date = models.DateField(auto_now_add=True)
    bag = models.IntegerField(default=0, verbose_name ="পরিমাণ")

    def __str__(self):
        return str(self.bag) + ' | Update: ' + str(self.date)

class DonationPhoto(models.Model):
    image = models.ImageField(upload_to='donation/', default = '', verbose_name = 'ছবি')
class Calender(models.Model):
    file = models.FileField(upload_to='calender/', default = '')
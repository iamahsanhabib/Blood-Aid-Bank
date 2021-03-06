# Generated by Django 3.2.3 on 2021-06-05 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Bloodbank', '0008_auto_20210605_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(default='', upload_to='calender/')),
            ],
        ),
        migrations.CreateModel(
            name='DailyDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('bag', models.IntegerField(default=0, verbose_name='পরিমাণ')),
            ],
        ),
        migrations.CreateModel(
            name='DonationPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='donation/', verbose_name='ছবি')),
            ],
        ),
        migrations.CreateModel(
            name='TotalDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('bag', models.IntegerField(default=0, verbose_name='পরিমাণ')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('চাঁদা', 'চাঁদা'), ('অনুদান', 'অনুদান'), ('অনান্য', 'অনান্য')], default='চাঁদা', max_length=100, verbose_name='বিবরণী')),
                ('amount', models.IntegerField(default=0, verbose_name='পরিমাণ')),
                ('month', models.CharField(choices=[('জানুয়ারি', 'জানুয়ারি'), ('ফেব্রুয়ারি', 'ফেব্রুয়ারি'), ('মার্চ', 'মার্চ'), ('এপ্রিল', 'এপ্রিল'), ('মে', 'মে'), ('জুন', 'জুন'), ('জুলাই', 'জুলাই'), ('আগস্ট', 'আগস্ট'), ('সেপ্টেম্বর', 'সেপ্টেম্বর'), ('অক্টোবর', 'অক্টোবর'), ('নভেম্বর', 'নভেম্বর'), ('ডিসেম্বর', 'ডিসেম্বর')], max_length=100, verbose_name='মাস')),
                ('date', models.DateField(auto_now_add=True, verbose_name='তারিখ')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.organizationmember', verbose_name='নাম')),
            ],
        ),
        migrations.CreateModel(
            name='Financial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('des', models.CharField(max_length=100, verbose_name='বিবরণী')),
                ('category', models.CharField(choices=[('জমা', 'জমা'), ('খরচ', 'খরচ')], max_length=100, verbose_name='ক্যাটেগরি')),
                ('amount', models.IntegerField(default=0, verbose_name='পরিমাণ')),
                ('month', models.CharField(choices=[('জানুয়ারি', 'জানুয়ারি'), ('ফেব্রুয়ারি', 'ফেব্রুয়ারি'), ('মার্চ', 'মার্চ'), ('এপ্রিল', 'এপ্রিল'), ('মে', 'মে'), ('জুন', 'জুন'), ('জুলাই', 'জুলাই'), ('আগস্ট', 'আগস্ট'), ('সেপ্টেম্বর', 'সেপ্টেম্বর'), ('অক্টোবর', 'অক্টোবর'), ('নভেম্বর', 'নভেম্বর'), ('ডিসেম্বর', 'ডিসেম্বর')], max_length=100, verbose_name='মাস')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.organizationmember', verbose_name='নাম')),
            ],
        ),
        migrations.CreateModel(
            name='BloodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, verbose_name='রক্তদাতা নাম')),
                ('phone1', models.CharField(max_length=14, verbose_name='রক্তদাতার নাম্বার')),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], default='Select', max_length=6, verbose_name='রক্তের গ্রুপ')),
                ('name2', models.CharField(max_length=100, verbose_name='রোগীর নাম')),
                ('problem', models.CharField(max_length=14, verbose_name='রোগীর সমস্যা')),
                ('phone2', models.CharField(max_length=14, verbose_name='রোগীর নাম্বার')),
                ('date', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=100, verbose_name='রক্তদানের স্থান')),
                ('bag', models.IntegerField(default=1, verbose_name='রক্তের পরিমাণ')),
                ('ref_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.organizationmember', verbose_name='রেফারেন্স')),
            ],
        ),
    ]

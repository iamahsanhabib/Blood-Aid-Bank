# Generated by Django 3.2.3 on 2021-06-07 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodbank', '0010_alter_booking_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='statement',
            field=models.CharField(blank=True, choices=[('সংগ্রহ চলছে', 'সংগ্রহ চলছে'), ('যোগাযোগ করুন', 'যোগাযোগ করুন')], max_length=100, verbose_name='রক্তের অবস্থা'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')], default='Select', max_length=6, verbose_name='রক্তের গ্রুপ'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='location',
            field=models.CharField(max_length=100, verbose_name='উপজেলা'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='zilla',
            field=models.CharField(max_length=100, verbose_name='জেলা'),
        ),
    ]
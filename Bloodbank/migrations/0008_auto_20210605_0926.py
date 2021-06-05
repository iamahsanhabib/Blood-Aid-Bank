# Generated by Django 3.2.3 on 2021-06-05 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodbank', '0007_about'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About BABJ'},
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='রক্তদাতা নাম')),
                ('phone', models.CharField(max_length=14, verbose_name='মোবাইল নাম্বার')),
                ('problem', models.CharField(max_length=100, verbose_name='রোগীর সমস্যা')),
                ('month', models.CharField(max_length=100, verbose_name='মাস')),
                ('week', models.CharField(choices=[('১ম', '১ম'), ('২য়', '২য়'), ('৩য়', '৩য়'), ('৪র্থ', '৪র্থ')], max_length=100, verbose_name='সপ্তাহ')),
                ('statement', models.CharField(choices=[('সংগ্রহ চলছে', 'সংগ্রহ চলছে'), ('যোগাযোগ করুন', 'যোগাযোগ করুন')], max_length=100, verbose_name='রক্তের অবস্থা')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.bloodgroup', verbose_name='রক্তের গ্রুপ')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.upazila', verbose_name='উপজেলা/থানা')),
                ('zilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.zilla', verbose_name='জেলা')),
            ],
            options={
                'verbose_name_plural': 'Blood Booking',
            },
        ),
    ]

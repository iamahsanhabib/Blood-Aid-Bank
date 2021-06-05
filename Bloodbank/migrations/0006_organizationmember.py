# Generated by Django 3.2.3 on 2021-06-05 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodbank', '0005_auto_20210605_0820'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.CharField(blank=True, max_length=15, null=True, verbose_name='আইডি নং-')),
                ('name', models.CharField(max_length=100, verbose_name='সদস্যের নাম')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Select', max_length=10, verbose_name='লিঙ্গ')),
                ('phone', models.CharField(max_length=14, verbose_name='মোবাইল নাম্বার')),
                ('institution', models.CharField(max_length=100, verbose_name='শিক্ষা-প্রতিষ্ঠান')),
                ('image', models.ImageField(default='', upload_to='Member/', verbose_name='ছবি')),
                ('blood_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.bloodgroup', verbose_name='রক্তের গ্রুপ')),
                ('designation', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.designation', verbose_name='পদবি')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.upazila', verbose_name='উপজেলা/থানা')),
                ('zilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.zilla', verbose_name='জেলা')),
            ],
            options={
                'verbose_name_plural': 'Member',
            },
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-05 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodbank', '0002_applicant_bloodgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodgroup',
            options={'verbose_name_plural': 'Blood Group'},
        ),
        migrations.AddField(
            model_name='applicant',
            name='blood_group',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.bloodgroup', verbose_name='রক্তের গ্রুপ'),
            preserve_default=False,
        ),
    ]

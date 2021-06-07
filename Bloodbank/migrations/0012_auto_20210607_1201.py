# Generated by Django 3.2.3 on 2021-06-07 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bloodbank', '0011_auto_20210607_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.upazila', verbose_name='উপজেলা/থানা'),
        ),
        migrations.AlterField(
            model_name='donor',
            name='zilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bloodbank.zilla', verbose_name='জেলা'),
        ),
    ]

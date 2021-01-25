# Generated by Django 3.0.6 on 2020-05-28 13:30

import django.core.validators
from django.db import migrations, models
import small_eod.generic.validators


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0009_auto_20200308_2139'),
        ('institutions', '0007_auto_20200221_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='address',
        ),
        migrations.RemoveField(
            model_name='institution',
            name='external_identifier',
        ),
        migrations.AddField(
            model_name='institution',
            name='city',
            field=models.CharField(blank=True, help_text='Name of city.', max_length=100, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='institution',
            name='email',
            field=models.EmailField(blank=True, help_text='E-mail address.', max_length=254, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='institution',
            name='epuap',
            field=models.CharField(blank=True, help_text='ePUAP address.', max_length=100, verbose_name='ePUAP'),
        ),
        migrations.AddField(
            model_name='institution',
            name='flat_no',
            field=models.CharField(blank=True, help_text='Flat number.', max_length=100, verbose_name='Flat number'),
        ),
        migrations.AddField(
            model_name='institution',
            name='house_no',
            field=models.CharField(blank=True, help_text='House number.', max_length=100, verbose_name='House number'),
        ),
        migrations.AddField(
            model_name='institution',
            name='nip',
            field=models.CharField(blank=True, help_text='Tax Identification Number.', max_length=10, validators=[small_eod.generic.validators.ExactLengthsValidator([10]), django.core.validators.RegexValidator('^[0-9]*$')], verbose_name='NIP'),
        ),
        migrations.AddField(
            model_name='institution',
            name='postal_code',
            field=models.CharField(blank=True, help_text='Postal code.', max_length=100, verbose_name='Postal code'),
        ),
        migrations.AddField(
            model_name='institution',
            name='regon',
            field=models.CharField(blank=True, help_text='Statistical Identification Number.', max_length=14, validators=[small_eod.generic.validators.ExactLengthsValidator([10, 14]), django.core.validators.RegexValidator('^[0-9]*$')], verbose_name='REGON'),
        ),
        migrations.AddField(
            model_name='institution',
            name='street',
            field=models.CharField(blank=True, help_text='Name of street.', max_length=100, verbose_name='Street'),
        ),
        migrations.DeleteModel(
            name='AddressData',
        ),
        migrations.DeleteModel(
            name='ExternalIdentifier',
        ),
    ]
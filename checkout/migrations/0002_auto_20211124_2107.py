# Generated by Django 3.2.9 on 2021-11-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='company_colors',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='company_description',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='company_look',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='company_name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='company_slogan',
            field=models.CharField(default=0, max_length=200),
        ),
    ]

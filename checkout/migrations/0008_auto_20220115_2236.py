# Generated by Django 3.2.9 on 2022-01-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20220114_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
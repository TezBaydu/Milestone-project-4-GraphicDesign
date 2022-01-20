from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_orderlogorequestdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='company_colors',
            field=models.CharField(default='Company Colors required', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='company_description',
            field=models.CharField(default='Company Description required', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='company_look',
            field=models.CharField(default='Company Look required', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='company_name',
            field=models.CharField(default='Company Name required', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='company_slogan',
            field=models.CharField(default='Company Slogan required', max_length=200),
        ),
        migrations.DeleteModel(
            name='OrderLogoRequestDetails',
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_remove_orderlineitem_company_details'),
        ('packages', '0006_auto_20211203_0107'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyDetails',
        ),
        migrations.AddField(
            model_name='package',
            name='company_colors',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='package',
            name='company_description',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='package',
            name='company_look',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='package',
            name='company_name',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='package',
            name='company_slogan',
            field=models.CharField(default=0, max_length=200),
        ),
    ]

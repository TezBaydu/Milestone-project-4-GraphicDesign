from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_companydetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

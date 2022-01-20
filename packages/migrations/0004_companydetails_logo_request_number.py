from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_companydetails_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='logo_request_number',
            field=models.CharField(default=0, editable=False, max_length=32),
            preserve_default=False,
        ),
    ]

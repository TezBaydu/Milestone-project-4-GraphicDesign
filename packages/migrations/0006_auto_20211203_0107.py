from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20211201_2139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companydetails',
            options={'verbose_name_plural': 'Company Details'},
        ),
        migrations.AlterField(
            model_name='companydetails',
            name='company_name',
            field=models.CharField(default=0, max_length=100),
        ),
    ]

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default=0, max_length=100)),
                ('company_slogan', models.CharField(default=0, max_length=200)),
                ('company_description', models.CharField(default=0, max_length=500)),
                ('company_colors', models.CharField(default=0, max_length=100)),
                ('company_look', models.CharField(default=0, max_length=100)),
            ],
        ),
    ]

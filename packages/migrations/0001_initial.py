from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('logo_count_request', models.IntegerField()),
                ('quality_request', models.TextField(blank=True, null=True)),
                ('support_request', models.TextField(blank=True, null=True)),
                ('production_days', models.IntegerField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]

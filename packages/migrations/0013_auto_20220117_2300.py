from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0012_auto_20220113_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='logo_count_request',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='production_days',
            field=models.DecimalField(decimal_places=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='package',
            name='quality_request',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='support_request',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

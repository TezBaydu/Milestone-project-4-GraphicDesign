from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0007_auto_20220112_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='company_colors',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_description',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_look',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_slogan',
            field=models.CharField(default=True, max_length=200),
        ),
    ]

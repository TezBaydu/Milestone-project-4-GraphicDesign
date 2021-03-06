from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20220113_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='company_colors',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='company_description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='company_look',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='company_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='company_slogan',
            field=models.CharField(max_length=200),
        ),
    ]

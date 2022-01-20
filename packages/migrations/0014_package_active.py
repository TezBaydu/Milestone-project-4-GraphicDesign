from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0013_auto_20220117_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]

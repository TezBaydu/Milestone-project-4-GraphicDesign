from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0011_auto_20220113_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='company_colors',
        ),
        migrations.RemoveField(
            model_name='package',
            name='company_description',
        ),
        migrations.RemoveField(
            model_name='package',
            name='company_look',
        ),
        migrations.RemoveField(
            model_name='package',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='package',
            name='company_slogan',
        ),
    ]

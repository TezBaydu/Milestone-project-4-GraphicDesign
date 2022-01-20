from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='company_details',
        ),
    ]

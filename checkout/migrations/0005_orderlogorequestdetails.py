from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_orderlineitem_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLogoRequestDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='Company Name required', max_length=100)),
                ('company_slogan', models.CharField(default='Company Slogan required', max_length=200)),
                ('company_description', models.CharField(default='Company Description required', max_length=500)),
                ('company_colors', models.CharField(default='Company Colors required', max_length=100)),
                ('company_look', models.CharField(default='Company Look required', max_length=100)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logoitems', to='checkout.order')),
            ],
        ),
    ]

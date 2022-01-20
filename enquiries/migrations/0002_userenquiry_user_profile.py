from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_full_name'),
        ('enquiries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userenquiry',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enquiries', to='profiles.userprofile'),
        ),
    ]

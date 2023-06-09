# Generated by Django 4.1.8 on 2023-05-02 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "referrals",
            "0002_userreferral_created_alter_userreferral_invite_code_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="userreferral",
            name="earnings",
            field=models.DecimalField(
                decimal_places=2, default=0.0, editable=False, max_digits=10
            ),
        ),
        migrations.AlterField(
            model_name="userreferral",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="referral_profile",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

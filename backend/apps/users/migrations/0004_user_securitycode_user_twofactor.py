# Generated by Django 5.1.5 on 2025-01-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='securitycode',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twofactor',
            field=models.BooleanField(default=False),
        ),
    ]

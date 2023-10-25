# Generated by Django 4.2.6 on 2023-10-25 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('massage', '0002_chatmassage_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmassage',
            name='recipient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='users.userprofile'),
        ),
    ]

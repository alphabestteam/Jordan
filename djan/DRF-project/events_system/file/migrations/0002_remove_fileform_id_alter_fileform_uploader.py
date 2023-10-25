# Generated by Django 4.2.6 on 2023-10-25 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userprofile_unread_messages_and_more'),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileform',
            name='id',
        ),
        migrations.AlterField(
            model_name='fileform',
            name='uploader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.userprofile'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

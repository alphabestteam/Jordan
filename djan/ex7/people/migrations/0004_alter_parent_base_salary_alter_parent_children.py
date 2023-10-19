# Generated by Django 4.2.6 on 2023-10-19 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_alter_person_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='base_salary',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(related_name='parents', to='people.person'),
        ),
    ]

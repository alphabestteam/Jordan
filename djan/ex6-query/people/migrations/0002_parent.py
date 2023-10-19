# Generated by Django 4.2.6 on 2023-10-17 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='people.person')),
                ('workplace', models.CharField(blank=True, max_length=100, null=True)),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('children', models.ManyToManyField(blank=True, related_name='parents', to='people.person')),
            ],
            bases=('people.person',),
        ),
    ]

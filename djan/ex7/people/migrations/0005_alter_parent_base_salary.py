

from django.db import migrations, models
from django.core.validators import MaxValueValidator


def validate_base_salary(apps, schema_editor):
    Parent = apps.get_model('people', 'Parent')
    db_alias = schema_editor.connection.alias
    Parent.objects.using(db_alias).exclude(
        base_salary__lte=999999
    ).update(base_salary=999999)


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_parent_base_salary_alter_parent_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='base_salary',
            field =models.IntegerField(validators=[MaxValueValidator(999999)])
        ),
         migrations.RunPython(validate_base_salary),
    ]

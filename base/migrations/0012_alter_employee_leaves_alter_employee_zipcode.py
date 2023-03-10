# Generated by Django 4.1.5 on 2023-01-27 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_employee_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='leaves',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zipcode',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-26 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_employee_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='leaves',
            field=models.IntegerField(default=0, null=True),
        ),
    ]

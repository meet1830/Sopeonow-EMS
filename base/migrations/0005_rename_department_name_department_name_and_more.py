# Generated by Django 4.1.5 on 2023-01-25 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_employee_zipcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='role_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='dept',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.department'),
        ),
    ]

# Generated by Django 4.2.4 on 2024-01-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0017_alter_payroll_employee_amountperhr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll_employee',
            name='amountperhr',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='payroll_employee',
            name='workhr',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

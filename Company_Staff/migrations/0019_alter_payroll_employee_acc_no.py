# Generated by Django 4.2.4 on 2024-01-19 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0018_alter_payroll_employee_amountperhr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll_employee',
            name='acc_no',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-19 22:59

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0006_alter_patient_department_alter_patient_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, region=None, unique=True
            ),
        ),
    ]

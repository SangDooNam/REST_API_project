# Generated by Django 5.0.3 on 2024-03-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0005_remove_patient_hair"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="department",
            field=models.CharField(
                choices=[
                    ("CARD", "Cardiology"),
                    ("NEUR", "Neurology"),
                    ("ORTH", "Orthopedics"),
                    ("PEDI", "Pediatrics"),
                    ("DERM", "Dermatology"),
                    ("EMER", "Emergency Medicine"),
                    ("OBGY", "Obstetrics and Gynecology"),
                    ("ONCO", "Oncology"),
                    ("PSYC", "Psychiatry"),
                    ("ENDO", "Endocrinology"),
                    ("GAST", "Gastroenterology"),
                    ("UROL", "Urology"),
                    ("PULM", "Pulmonology"),
                    ("INF", "Infectious Diseases"),
                    ("RHEU", "Rheumatology"),
                    ("HEMA", "Hematology"),
                    ("NEPH", "Nephrology"),
                    ("ALLI", "Allergy and Immunology"),
                    ("GERI", "Geriatrics"),
                    ("OPHT", "Ophthalmology"),
                    ("OTOL", "Otolaryngology"),
                    ("PLAS", "Plastic Surgery"),
                    ("REHA", "Rehabilitation Medicine"),
                    ("NEON", "Neonatology"),
                    ("SPME", "Sports Medicine"),
                    ("PATH", "Pathology"),
                    ("RADI", "Radiology"),
                    ("ANES", "Anesthesiology"),
                    ("PHTH", "Physical Therapy"),
                    ("DENT", "Dentistry"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="email",
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
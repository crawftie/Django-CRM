# Generated by Django 4.2.4 on 2023-09-14 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_doctor_record_doctor_specialism_hospital_record_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Record',
        ),
        migrations.AlterField(
            model_name='doctor_record',
            name='doctor_specialism',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.doctor_specialism'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-28 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_student_average'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='hasScholarship',
        ),
    ]
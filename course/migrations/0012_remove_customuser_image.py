# Generated by Django 4.2.4 on 2024-04-27 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_customuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
    ]

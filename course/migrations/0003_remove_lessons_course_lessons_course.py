# Generated by Django 4.2.4 on 2024-04-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_lessons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='course',
        ),
        migrations.AddField(
            model_name='lessons',
            name='course',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=30)),
                ('coursecode', models.CharField(blank=True, max_length=5, null=True)),
                ('level', models.CharField(blank=True, max_length=3, null=True)),
                ('duration', models.CharField(blank=True, max_length=20, null=True)),
                ('fee', models.CharField(blank=True, max_length=25, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

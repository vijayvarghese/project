# Generated by Django 3.2.16 on 2024-01-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input1', models.CharField(max_length=255)),
                ('input2', models.CharField(max_length=255)),
                ('rich_input', models.TextField()),
            ],
        ),
    ]

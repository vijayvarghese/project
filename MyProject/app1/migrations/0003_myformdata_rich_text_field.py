# Generated by Django 3.2.16 on 2024-01-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_myformdata_rich_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='myformdata',
            name='rich_text_field',
            field=models.TextField(default=''),
        ),
    ]

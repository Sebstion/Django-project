# Generated by Django 4.2.6 on 2023-11-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='haslo', max_length=20),
            preserve_default=False,
        ),
    ]

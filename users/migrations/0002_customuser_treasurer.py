# Generated by Django 2.1.1 on 2018-08-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='treasurer',
            field=models.BooleanField(default=False),
        ),
    ]
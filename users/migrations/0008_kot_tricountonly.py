# Generated by Django 2.2.5 on 2019-09-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_internal'),
    ]

    operations = [
        migrations.AddField(
            model_name='kot',
            name='tricountOnly',
            field=models.BooleanField(default=False),
        ),
    ]
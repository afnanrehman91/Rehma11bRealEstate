# Generated by Django 2.1.4 on 2018-12-05 01:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eproperty', '0006_auto_20181205_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='propertyConstructionDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='property',
            name='propertyRegistrationDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

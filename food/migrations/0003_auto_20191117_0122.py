# Generated by Django 2.2.7 on 2019-11-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20191117_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_amount',
            field=models.IntegerField(default=0),
        ),
    ]

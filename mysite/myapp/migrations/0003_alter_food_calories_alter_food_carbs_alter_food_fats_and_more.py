# Generated by Django 4.0.6 on 2022-08-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_consume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='fats',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.FloatField(),
        ),
    ]
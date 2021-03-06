# Generated by Django 3.0.7 on 2020-07-07 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200706_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='color',
            field=models.CharField(choices=[('C_ONE', 'Color 1'), ('C_TWO', 'Color 2')], default='C_ONE', max_length=25),
        ),
        migrations.AlterField(
            model_name='card',
            name='font',
            field=models.CharField(choices=[('F_ONE', 'Font 1'), ('F_TWO', 'Font 2')], default='F_ONE', max_length=25),
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-13 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kassa', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OperationNameMinus',
        ),
        migrations.AddField(
            model_name='operationname',
            name='type',
            field=models.CharField(default='plus', max_length=255),
        ),
    ]

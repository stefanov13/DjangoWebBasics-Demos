# Generated by Django 4.2.1 on 2023-05-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default='shumen', max_length=50),
            preserve_default=False,
        ),
    ]

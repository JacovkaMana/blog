# Generated by Django 4.1.1 on 2022-10-10 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamegen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='god',
            name='god_color',
            field=models.CharField(default='000000', max_length=7),
        ),
    ]

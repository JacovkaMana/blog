# Generated by Django 4.1.1 on 2022-10-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=None, verbose_name='date_published'),
        ),
    ]
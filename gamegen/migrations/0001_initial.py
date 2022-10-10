# Generated by Django 4.1.1 on 2022-10-10 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modificator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modificator_name', models.CharField(max_length=42)),
                ('modificator_rarity', models.IntegerField(choices=[(1, 'Common'), (2, 'Uncommon'), (3, 'Rare'), (4, 'Epic'), (5, 'Legendary')])),
                ('modificator_color', models.CharField(max_length=7)),
                ('modificator_stats', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_name', models.CharField(max_length=42)),
                ('title_alignment', models.CharField(max_length=42)),
                ('title_color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='God',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('god_generated', models.BooleanField(default=False)),
                ('god_modificator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamegen.modificator')),
                ('god_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamegen.title')),
            ],
        ),
    ]

import datetime

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


"""
RARITY_CHOISE = [
    (COMMON, 'Common'),
    (UNCOMMON, 'Uncommon'),
    (RARE, 'Rare'),
    (EPIC, 'Epic'),
    (LEGENDARY, 'Legendary'),
]
"""

class Rarity(models.IntegerChoices):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class Modificator(models.Model):
    modificator_name = models.CharField(max_length=42)
    modificator_rarity = models.IntegerField(choices=Rarity.choices)
    modificator_color = models.CharField(max_length = 7)
    modificator_stats = models.CharField(max_length = 4)


    def __str__(self):
        return self.modificator_name


class Title(models.Model):
    title_name = models.CharField(max_length=42)
    title_alignment = models.CharField(max_length=42)
    title_color = models.CharField(max_length = 7)

    def __str__(self):
        return self.title_name 

class God(models.Model):
    god_modificator = models.ForeignKey(Modificator, on_delete=models.CASCADE)
    god_title = models.ForeignKey(Title, on_delete=models.CASCADE)
    god_generated = models.BooleanField(default = False)
    god_color = models.CharField(max_length = 7, default = '000000')


# Create your models here.

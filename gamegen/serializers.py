# capitals/serializers.py
from rest_framework import serializers

from .models import Title, Modificator
from django.contrib.auth.models import User, Group

class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = ['url', 'title_name', 'title_color']


class ModificatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Modificator
        fields = ['url', 'modificator_name']
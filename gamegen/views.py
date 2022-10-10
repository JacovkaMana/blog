from django.shortcuts import render


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

#from blog.posts.forms import CommentForm

from django.contrib.auth.models import User, Group

from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions

from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from gamegen import serializers
# Create your views here.
from .mygenerator import code
from .models import God, Title, Modificator

from django.http import JsonResponse
from django.core import serializers
import json
from django.forms.models import model_to_dict
import random

def dec_to_hex(list):
    s = ''
    for c in list:
        d = hex(c)[2:]
        if len(d) == 1:
            d = '0'+ d
        s += d
    return s

def hex_summ(string1, string2):
    s = ''
    for i in range(0, 6, 2):
        a = int(string1[i : i + 2], 16)
        b = int(string2[i : i + 2], 16)
        c = (a + b) // 2
        s += hex(c)[2:]
    return s

def stats_to_str(stats):
    s = ''
    for i in stats:
        s += str(i)
    return s

def test_generate(request):
    code.start('static\posts\modificators.json')
    return HttpResponse('success')


def show_random_god(request):
    title_len = list(Title.objects.all())
    modifiers_len = list(Modificator.objects.all())
    title = random.choice(title_len)
    modifier = random.choice(modifiers_len)
    god = God()
    god.god_modificator = modifier
    god.god_title = title
    s = ''
    for i in range(0, 6, 2):
        a = int(modifier.modificator_color[i : i + 2], 16)
        b = int(title.title_color[i : i + 2], 16)
        c = (a + b) // 2
        print(a, b, c)
        d = hex(c)[2:]
        if len(d) == 1:
            d = '0'+ d
        s += d
        print(s)
    god.god_color = s
    #return HttpResponse(serialized)
    return render(request, 'gamegen/base.html', {'title':  title, 'modifier' : modifier, 'god' : god})


def reload_json(request):
    with open('static\posts\modificators.json') as json_file:
        data = json.load(json_file)
    for i in range(len(data['modificators'])):
        mod = data['modificators'][i]
        if (len(Modificator.objects.filter(modificator_name=mod['name']))) == 0:
            n_modifier = Modificator()
            n_modifier.modificator_name = mod['name']
            n_modifier.modificator_rarity = mod['rarity']
            n_modifier.modificator_color = dec_to_hex(mod['color'])
            n_modifier.modificator_stats = stats_to_str(mod['stats'])
            n_modifier.save()
    for i in range(len(data['names'])):
        mod = data['names'][i]
        if (len(Title.objects.filter(title_name=mod['name']))) == 0:
            n_modifier = Title()
            n_modifier.title_name = mod['name']
            n_modifier.title_alignment = mod['alignment']
            n_modifier.title_color = dec_to_hex(mod['color'])
            n_modifier.save()

    
    return HttpResponse('serialized')
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core import serializers


# Create your views here.

def get_data_in_json_format(request):
    return HttpResponse(serializers.serialize('json', Notice.objects.all()))

from django.shortcuts import render, redirect
from .models import *
from django.db import IntegrityError
import datetime

def index(request):
    return render(request, 'main/index.html')

def add(request):
    return render(request, 'main/add.html')
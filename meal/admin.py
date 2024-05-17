"""admin.py"""
from django.contrib import admin
from .models import Frequency, Unit

admin.site.register(Frequency)
admin.site.register(Unit)

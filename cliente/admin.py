# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cliente, Duplicata

admin.site.register(Cliente)
admin.site.register(Duplicata)

# Register your models here.

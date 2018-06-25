# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cell, Objectives, Member
# Register your models here.
admin.site.register(Cell)
admin.site.register(Member)
admin.site.register(Objectives)

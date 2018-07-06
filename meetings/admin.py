# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cell, Objective, Member, Meeting
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

# Register your models here.
admin.site.register(Cell)
admin.site.register(Member)
admin.site.register(Objective)
admin.site.register(Meeting)

class EntityAdmin(admin.ModelAdmin):
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )

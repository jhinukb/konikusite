# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class ValidFieldsTestCase(TestCase):
    def setup(self):
        c = Cell.objects.create(cell_name = 'TempCell')
        m = Member.objects.create(member_name='Billy', email='ok@bye.com', cell = c)
        CellForm.objects.create(cell = c, member = m)

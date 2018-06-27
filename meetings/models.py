# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Cell(models.Model):
	cell_name = models.CharField(max_length=200)
	def __str__(self):
		return self.cell_name

class Member(models.Model):
	member_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
	def __str__(self):
		return self.member_name
	def get_email(self):
		return self.email

class Objective(models.Model):
	text = models.CharField(max_length=400)
	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.objective_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=14) <= self.pub_date <= now

class CellForm(models.Model):
	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

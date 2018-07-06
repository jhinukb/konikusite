# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Cell(models.Model):
	cell_name = models.CharField(max_length=200)
	#members = models.ManyToManyField(Member)
	def __str__(self):
		return self.cell_name
	class Meta:
	     ordering = ('cell_name',)

class Member(models.Model):
	member_name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	cells = models.ManyToManyField(Cell)
	def __str__(self):
		return self.member_name
	def get_email(self):
		return self.email
	class Meta:
	     ordering = ('member_name',)


class Objective(models.Model):
	objective_text = models.CharField(max_length=400, default = 'val')
	cell = models.ForeignKey(Cell, on_delete=models.CASCADE) #or obj can be connected to Meeting model
	completion_status = models.CharField(max_length=400, default = 'val')
	incompletion_reason = models.CharField(max_length=400, default = 'val')
	changed_reason = models.CharField(max_length=400, default = 'val')
	#expected supply arrival date
	exp_supply_dt = models.DateTimeField(default=timezone.now)
	#expected objective completion date
	exp_obj_dt = models.DateTimeField(default=timezone.now)
	owner = models.CharField(max_length=400, default = 'val')
	cell_output = models.CharField(max_length=400, default = 'default cell output text')
	def __str__(self):
		return self.objective_text

class Meeting(models.Model):
	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	#Time
	date_recorded = models.DateTimeField(default=timezone.now)
        def was_published_recently(self):
			now = timezone.now()
			return now - datetime.timedelta(days=14) <= self.date_recorded <= now
	#Members (check: members are in the cell)
	#members = models.ForeignKey(Member, on_delete=models.CASCADE)
	#Objective (text)
	#next meeting date input
	objectives = models.ForeignKey(Objective, on_delete=models.CASCADE)
	next_meeting_date = models.DateTimeField(default=timezone.now)


# class CellForm(models.Model):
# 	cell_form_name = models.CharField(max_length=200, default = 'placeholder name')
# 	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
# 	member = models.ForeignKey(Member, on_delete=models.CASCADE)

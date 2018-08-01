  # -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

VAL_CHOICES=[('valid_nocom','Validated without comment'),
         ('valid_com','Validated with comments'),
         ('no_val', 'Cannot yet be validated')]
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

class WorkReview(models.Model):
	title = models.CharField(max_length=500, default="title def")
	file_location = models.CharField(max_length=500)
	validate = models.CharField(max_length=500, choices=VAL_CHOICES)
	content_val = models.TextField(default='def val')
	# valid_com_txt = models.TextArea(default="val")
	# no_valid_txt = models.TextArea(default="val")
	# validate = models.BooleanField('Validation: ', default=True)
	# valid_nocom = models.CharField(max_length=500, default="val")
	# no_val = models.CharField(max_length=500, default="val")
	def __str__(self):
		return self.file_location

	# def val_text(self):
	#     if self.validate == 'Validated with comments':
	# 		# display textbox
	# 		return valid_com_txt
	# 	elif self.validate == 'Cannot yet be validated':
	# 		return no_valid_txt
	# 	else:
	# 		return ''

class Meeting(models.Model):
	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	attendee_list = models.BooleanField(default=False)
	#Time
	date_recorded = models.DateTimeField(default=timezone.now)
        def was_published_recently(self):
			now = timezone.now()
			return now - datetime.timedelta(days=14) <= self.date_recorded <= now
	next_meeting_date = models.DateTimeField(default=timezone.now)
	# work_review = models.ForeignKey(WorkReview, on_delete=models.CASCADE)

# class CellForm(models.Model):
# 	cell_form_name = models.CharField(max_length=200, default = 'placeholder name')
# 	cell = models.ForeignKey(Cell, on_delete=models.CASCADE)
# 	member = models.ForeignKey(Member, on_delete=models.CASCADE)

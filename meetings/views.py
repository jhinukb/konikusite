# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Cell, Objective, Member, Meeting
from .forms import MeetingForm
#from django import forms
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse

def load_members(request):
    return 'hi'
    #cell_id = request.GET.get('cell')
    # members = Member.objects.filter(cell_id=cell_id).order_by('member_name')
    # #return cell
    # return render(request, 'meetings/meeting_dropdown_list_options.html', {'members': members})

#testing this out for checkboxes of attendee list
# def load_attendees(request):
#     cell_name = request.GET.get('cell')
#     members = Member.objects.filter(cell_name=cell_name).order_by('member_name')
#     return render(request, 'meetings/memberName_checkbox.html', {'members': members})

def index(request):
    #template_name = 'meetings/index.html'
    return HttpResponse("Hello, world. You're at the meetings index.")

class MeetingFormPage(FormView):
    Model = Meeting
    template_name = 'meetings/cell_form.html'
    #fields = ('cell', 'member')
    success_url = reverse_lazy('cell_form')
    form_class = MeetingForm

    def form_valid(self, form):
        return HttpResponse("Success!")


# class CellListView(ListView):
#     model = Cell
#     context_object_name = 'cell_name'
#     form_class = CellForm
#
#     def load_cellNames(request):
#         cell_id = request.GET.get('Name')
#         cellNames = Cell.objects.filter(id=cell)
#         #return HttpResponse("Hello, world. You're at the meetings loadcells page.")
#
#         return render(request, 'meetings/templates/cellName_dropdown_list_options.html', {'Name': cellNames})

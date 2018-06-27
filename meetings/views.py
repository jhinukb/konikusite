# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Cell, CellForm, Objective, Member
from .forms import CellForm
from django import forms
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse

def load_members(request):
    cell = request.GET.get('cell')
    members = Member.objects.filter(cell=cell).order_by('member_name')
    return render(request, 'meeting/cellName_dropdown_list_options.html', {'members': members})

def index(request):
    template_name = 'meetings/index.html'
    return HttpResponse("Hello, world. You're at the meetings index.")

class CellFormPage(FormView):
    Model = Cell
    template_name = 'meetings/cell_form.html'
    fields = ('cell_name',)
    success_url = reverse_lazy('cell_form')
    form_class = CellForm

    def form_valid(self, form):
        return HttpResponse("Sweeeeeet.")
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

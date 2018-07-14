# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Cell, Objective, Member, Meeting
from .forms import MeetingForm
from django.urls import reverse
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

def load_members(request):
    cell_id = request.GET.get('cell')
    members = Member.objects.filter(cells=cell_id).order_by('member_name')
    return render(request, 'meetings/cell_dropdown_list_options.html', {'members': members})

def work_review(request):
    # cell_id = request.GET.get('cell')
    # members = Member.objects.filter(cells=cell_id).order_by('member_name')
    return render(request, 'meetings/work_review.html')
    #return render(request, 'meetings/work_review.html', {'members': members})

#testing this out for checkboxes of attendee list
def load_attendees(request):
    cell_id = request.GET.get('cell')
    #cell = Cell.objects.get(id=cell_id)
    #member = member.cell.all().values('name', 'id')

    members = Member.objects.filter(cells=cell_id).order_by('member_name')
    return render(request, 'meetings/memberName_checkbox.html', {'members': members})

def index(request):
    #template_name = 'meetings/index.html'
    return HttpResponse("Hello, world. You're at the meetings index.")

class MeetingFormPage(FormView):
    Model = Meeting
    template_name = 'meetings/cell_form.html'
    fields = ('cell', 'member')
    success_url = reverse_lazy('cell_form')
    form_class = MeetingForm

    def form_valid(self, form):
        #string inside reverse refers to another view function
        return HttpResponseRedirect(reverse('work_review')) #currently goes back to same page
        #return HttpResponse("Success!")

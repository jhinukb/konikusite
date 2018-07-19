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


# def work_review(request):
#     return render(request, 'meetings/work_review.html')

class WorkReview(FormView):
    Model = Meeting
    template_name = 'meetings/work_review.html'
    fields = ('cell', 'member')
    success_url = reverse_lazy('work_review')
    form_class = MeetingForm
    def form_valid(self, form):
    #     #string inside reverse refers to another view/url function
        return HttpResponseRedirect(reverse('objectives'))
        #return HttpResponse("Success!")

def objectives(request):
    #return HttpResponse("Objectives Pageee.")
    return render(request, 'meetings/objectives.html')

#testing this out for checkboxes of attendee list
# def load_attendees(request):
#     cell_id = request.GET.get('cell')
#     members = Member.objects.filter(cells=cell_id).order_by('member_name')
#     return render(request, 'meetings/memberName_checkbox.html', {'members': members})
#
# def index(request):
#     template_name = 'meetings/index.html'
#     return HttpResponse("Hello, world. You're at the meetings index.")

class MeetingFormPage(FormView):
    Model = Meeting
    template_name = 'meetings/cell_form.html'
    fields = ('cell', 'member')
    success_url = reverse_lazy('cell_form')
    form_class = MeetingForm

    # form = MeetingForm(request.POST)
    # post.user = request.USER
    # post.save()
    # text = form.cleaned_data['post']
    # form = MeetingForm()
    def form_valid(self, form):
        #string inside reverse refers to another view/url function
        return HttpResponseRedirect(reverse('work_review')) #goes to work review url
        #return HttpResponse("Success!")

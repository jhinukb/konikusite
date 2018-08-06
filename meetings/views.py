# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Cell, Objective, Member, Meeting, WorkReview
from .forms import MeetingForm, WorkReviewForm, ObjectiveForm
from django.urls import reverse
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect

def load_members(request):
    cell_id = request.GET.get('cell')
    members = Member.objects.filter(cells=cell_id).order_by('member_name')
    if request.method == 'POST':
        if request.POST.get('cell') and request.POST.get('member'):
            meeting = Meeting()
            meeting.cell = request.POST.get('cell')
            meeting.member = request.POST.get('member')
            meeting.save()
    return render(request, 'meetings/cell_dropdown_list_options.html', {'members': members})

class ObjectivePage(FormView):
    Model = Objective
    template_name = 'meetings/objectives.html'
    fields = ('objective_text', 'owner', 'completion_status')
    success_url = reverse_lazy('objectives')
    form_class = ObjectiveForm
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            txt = form.cleaned_data['objective_text']
            owner = form.cleaned_data['owner']
            status = form.cleaned_data['completion_status']
            form = ObjectiveForm()
            # return render(request, self.template_name, args)
            return HttpResponseRedirect(reverse('objectives'))
        # args = {'form': form, 'txt': txt, 'owner': owner, 'status': status}
        # return render(request, self.template_name, args)
        # return HttpResponseRedirect(reverse('work_review'))

class WorkReviewPage(FormView):
    Model = WorkReview
    template_name = 'meetings/work_review.html'
    fields = ('file_location', 'validate')
    success_url = reverse_lazy('work_review')
    form_class = WorkReviewForm
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            text = form.cleaned_data['file_location']
            txt2 = form.cleaned_data['validate']
            form = WorkReviewForm()
            return HttpResponseRedirect(reverse('objectives')) #return HttpResponseRedirect(reverse('objectives'))
        args = {'form': form, 'text': text, 'txt2': txt2}
        return HttpResponseRedirect(reverse('objectives'))
        # return render(request, self.template_name, args)

    def create_file_loc(request):
        formset = WorkReviewFormSet(request.POST)
        for form in formset:
            text = form.cleaned_data.get('file_location')
            if text:
                WorkReview(file_location=text).save()
        return render(request, self.template_name, {'formset': formset})

# class WorkReviewPage(FormView):
#     Model = WorkReview
#     template_name = 'meetings/work_review.html'
#     fields = ('file_location', 'validate')
#     success_url = reverse_lazy('work_review')
#     form_class = WorkReviewForm
#     def form_valid(self, form):
#         if form.is_valid():
#             form.save()
#             text = form.cleaned_data['file_location']
#             txt2 = form.cleaned_data['validate']
#             form = WorkReviewForm()
#             return HttpResponseRedirect(reverse('objectives')) #return HttpResponseRedirect(reverse('objectives'))
#         args = {'form': form, 'text': text, 'txt2': txt2}
#         return HttpResponseRedirect(reverse('objectives'))
#         # return render(request, self.template_name, args)
#
#     def create_file_loc(request):
#         formset = WorkReviewFormSet(request.POST)
#         for form in formset:
#             text = form.cleaned_data.get('file_location')
#             if text:
#                 WorkReview(file_location=text).save()
#         return render(request, self.template_name, {'formset': formset})

def objectives(request):
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
    # def form_valid(self, form):
    #     #string inside reverse refers to another view/url function
    #     return HttpResponseRedirect(reverse('work_review')) #goes to work review url
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            text = form.cleaned_data['cell']
            # member = form.cleaned_data['member']
            form = WorkReviewForm()
            return HttpResponseRedirect(reverse('work_review'))        # return HttpResponseRedirect(reverse('objectives'))
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
        # return HttpResponseRedirect(reverse('work_review'))

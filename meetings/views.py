# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Cell, Objective, Member, Meeting, WorkReview
from .forms import MeetingForm, WorkReviewForm
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

# def val_text(request):
#     val_choice = request.GET.get('validate')
#     if val_choice

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
            return HttpResponseRedirect(reverse('work_review'))        # return HttpResponseRedirect(reverse('objectives'))
        args = {'form': form, 'text': text, 'txt2': txt2}
        return render(request, self.template_name, args)
        #return HttpResponse("Success!")
        # def file_loc(self, request):
        #     if form.is_valid():
        #         form.save()
        #         text = form.cleaned_data['post']
        #         form = HomeForm()
        #         return redirect('home:home')

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
    # def form_valid(self, form):
    #     #string inside reverse refers to another view/url function
    #     return HttpResponseRedirect(reverse('work_review')) #goes to work review url
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            text = form.cleaned_data['cell']
            form = WorkReviewForm()
            return HttpResponseRedirect(reverse('work_review'))        # return HttpResponseRedirect(reverse('objectives'))
        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

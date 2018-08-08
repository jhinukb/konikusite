# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic import FormView
from .models import Cell, Objective, Member, WorkReview, Meeting
from .forms import WorkReviewForm, ObjectiveForm, MeetingForm
from django.urls import reverse
# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

# FORMS = [("meeting", MeetingForm),
#          ("workreview",WorkReviewForm),
#          ("objective", ObjectiveForm)]
#
# TEMPLATES = {"meeting": "meetings/cell_form.html",
#              "workreview": "meetings/work_review.html",
#              "objective": "meetings/objectives.html"}
#
# class MeetingWizard(SessionWizardView):
#     def get_template_names(self):
#         return [TEMPLATES[self.steps.current]]
#
#     def done(self, form_list, form_dict, **kwargs):
#         # do_something_with_the_form_data(form_list)
#         cell = form_dict['cell'].save()
#         member = form_dict['member'].save()
#         return HttpResponseRedirect('objectives')

def load_members(request):
    cell_id = request.GET.get('cell')
    members = Member.objects.filter(cells=cell_id).order_by('member_name')
    attendee_list = Member.objects.filter(cells=cell_id).order_by('member_name')
    if request.method == 'POST':
        if request.POST.get('cell') and request.POST.get('member'):
            meeting = Meeting()
            meeting.cell = request.POST.get('cell')
            meeting.member = request.POST.get('member')
            meeting.attendee_list = request.POST.get('attendee_list')
            meeting.save()
    return render(request, 'meetings/cell_dropdown_list_options.html', {'members': members})

def objective_review(request):
    # return render(request, 'meetings/cell_dropdown_list_options.html', {'members': members})
    obj_data = Objective.objects.latest('id')
    cell = request.session['cell_id']
    #next 3 lines commented out in working version
    # obj_data = {
    # "obj_latest": obj,
    # }
    # return render(request, 'meetings/objectives_review.html', {'obj_data': obj_data})
    # return render_to_response("meetings/objectives_review.html", obj_data, context_instance=RequestContext(request))
    return HttpResponse(cell)


class ObjectivePage(FormView):
    Model = Objective
    template_name = 'meetings/objectives.html'
    # fields = ('objective_text', 'owner', 'completion_status')
    success_url = reverse_lazy('objectives')
    form_class = ObjectiveForm
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            txt = form.cleaned_data['objective_text']
            # owner = form.cleaned_data['owner']
            # status = form.cleaned_data['completion_status']
            form = ObjectiveForm()
            # return render(request, self.template_name, args)
            return HttpResponseRedirect(reverse('objectives_review'))
        # args = {'form': form, 'txt': txt, 'owner': owner, 'status': status}
        # return render(request, self.template_name, args)
        # return HttpResponseRedirect(reverse('work_review'))

class WorkReviewPage(FormView):
    Model = WorkReview
    template_name = 'meetings/work_review.html'
    # fields = ('file_location', 'validate', 'meeting', 'member')
    success_url = reverse_lazy('work_review')
    form_class = WorkReviewForm
    def form_valid(self, form):
        if form.is_valid():
            # form.cleaned_data['meeting'] = Meeting.objects.last() #this line isnt working properly
            form.save()
            text = form.cleaned_data['file_location']
            txt2 = form.cleaned_data['validate']
            # meeting = Meeting.objects.last()
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
#
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
        # return HttpResponseRedirect(reverse('work_review'))

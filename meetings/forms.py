from django import forms
from django.forms import ModelForm, Textarea, formset_factory, widgets
from meetings.models import Cell, Objective, Member, Meeting, WorkReview

COMP_CHOICES = [('complete', 'complete'),
		 ('incomplete', 'incomplete'),
		 ('changed', 'changed')]

# class HorizontalRadioRenderer(forms.RadioSelect.renderer):
#   def render(self):
#     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class ObjectiveForm(forms.ModelForm):
    class Meta:
        model = Objective
        fields = ('member1', 'res1', 'member2', 'res2', 'objective_text')
    objective_text = forms.CharField(widget=forms.Textarea)
    res1 = forms.CharField(max_length=400)
    res2 = forms.CharField(max_length=400)
    # owner = forms.CharField(max_length=500)
    def __init__(self, *args, **kwargs):
        super(ObjectiveForm, self).__init__(*args, **kwargs)
        meeting = Meeting.objects.last()
        # self.meeting = Meeting.objects.last()
        self.fields['member1'].queryset = Member.objects.filter(cells=meeting.cell.id).order_by('member_name')
        self.fields['member2'].queryset = Member.objects.filter(cells=meeting.cell.id).order_by('member_name')
        self.fields['member1'].label = "Select Objective Owner"
        self.fields['member2'].label = "Second Objective Owner?"
        self.fields['res1'].label = "% Responsibility"
        self.fields['res2'].label = "% Responsiblity"


    # completion_status = forms.ChoiceField(choices=COMP_CHOICES, widget=forms.RadioSelect())

VAL_CHOICES=[('valid_nocom','Validated without comment'),
         ('valid_com','Validated with comments'),
         ('no_val', 'Cannot yet be validated')]
#member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=cell.members)

class WorkReviewForm(forms.ModelForm):
    class Meta:
        model = WorkReview
        fields = ('file_location', 'validate', 'content_val', 'member')# 'valid_com', 'valid_nocom', 'no_val')
	file_location = forms.CharField(max_length=500)
    validate = forms.ChoiceField(choices=VAL_CHOICES, widget=forms.RadioSelect())
    content_val = forms.CharField(widget=forms.Textarea)
    meeting = Meeting.objects.latest(field_name='id') #this line is being used
    # member = Member.objects.filter(cells=meeting.cell.id).order_by('member_name')
    # meeting.widget = meeting.hidden_widget()
    def __init__(self, *args, **kwargs):
        super(WorkReviewForm, self).__init__(*args, **kwargs)
        # meeting = Meeting.objects.last()
        # self.meeting = Meeting.objects.last()
        self.fields['member'].queryset = Member.objects.filter(cells=self.meeting.cell.id).order_by('member_name')

    def add_fields(self):
        super(WorkReviewForm, self).add_fields(self)
        form.fields['myField'] = forms.CharField()
    # def __init__(self, *args, **kwargs):
        # super(WorkReviewForm, self).__init__(*args, **kwargs)
        # self.fields['member'].queryset = Member.objects.filter(cells=self.meeting.cell.id)


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('cell', 'member')
    # attendee_list = forms.CheckboxSelectMultiple()
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        #sets fields initially to nothing for members
        self.fields['member'].queryset = Member.objects.none()
        if 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['member'].queryset = Member.objects.filter(cells=cell_id).order_by('member_name')
                # self.fields['attendee_list'].queryset = forms.MultipleChoiceField(
                #     label="attendees",
                #     required=False,
                #     help_text="Select Meeting Attendees",
                #     widget=forms.CheckboxSelectMultiple,
                #     choices=Member.objects.filter(cells=cell_id).order_by('member_name'),
                #     )
                #self.fields['attendee_list'].queryset = Member.objects.filter(cells=cell_id).order_by('member_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Member queryset
        elif self.instance.pk:
            self.fields['member'].queryset = self.instance.cell.member_set.order_by('member_name')

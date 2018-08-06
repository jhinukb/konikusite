from django import forms
from django.forms import ModelForm, Textarea, formset_factory
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
        fields = ('objective_text', 'owner', 'completion_status')
    objective_text = forms.CharField(widget=forms.Textarea)
    owner = forms.CharField(max_length=500)

    # completion_status = forms.ChoiceField(choices=COMP_CHOICES, widget=forms.RadioSelect())

VAL_CHOICES=[('valid_nocom','Validated without comment'),
         ('valid_com','Validated with comments'),
         ('no_val', 'Cannot yet be validated')]
#member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=cell.members)

class WorkReviewForm(forms.ModelForm):
    class Meta:
        model = WorkReview
        fields = ('file_location', 'validate', 'content_val')# 'valid_com', 'valid_nocom', 'no_val')
	file_location = forms.CharField(max_length=500)
    validate = forms.ChoiceField(choices=VAL_CHOICES, widget=forms.RadioSelect())
    content_val = forms.CharField(widget=forms.Textarea)
    def add_fields(self):
        super(WorkReviewForm, self).add_fields(self)
        form.fields['myField'] = forms.CharField()
    # def __init__(self, *args, **kwargs):
    #     super(WorkReviewForm, self).__init__(*args, **kwargs)
    #     self.fields['content_val'].initial = 'Enter comments here.'
    #     self.fields['content_noVal'].initial = 'Enter why this work cannot yet be validated.'
# WorkReviewFormSet = formset_factory(WorkReviewForm, extra=1)

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('cell', 'member', 'attendee_list')
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        #sets fields initially to nothing for members
        self.fields['member'].queryset = Member.objects.none()
        if 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['member'].queryset = Member.objects.filter(cells=cell_id).order_by('member_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Member queryset
        elif self.instance.pk:
            self.fields['member'].queryset = self.instance.cell.member_set.order_by('member_name')

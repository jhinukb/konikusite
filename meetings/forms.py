from django import forms
from meetings.models import Cell, Objective, Member, Meeting, WorkReview

# CELL_CHOICES = [
#     ('tim', 'TIM'),
#     ('crispr', 'CRISPR'),
#     ('lotus', 'Lotus'),
#     ]
VAL_CHOICES=[('valid_nocom','Validated without comment'),
         ('valid_com','Validated with comments'),
         ('no_val', 'Cannot yet be validated')]
#member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=cell.members)
class WorkReviewForm(forms.ModelForm):
    class Meta:
        model = WorkReview
        fields = ('file_location', 'validate')# 'valid_com', 'valid_nocom', 'no_val')
	file_location = forms.CharField(max_length=500)
    validate = forms.ChoiceField(choices=VAL_CHOICES, widget=forms.RadioSelect())
	# valid_com = forms.CharField(max_length=500)
	# valid_nocom = forms.CharField(max_length=500)
	# no_val = forms.CharField(max_length=500)

class MeetingForm(forms.ModelForm):
    # cell = forms.CharField(max_length=100)
    # member = forms.CharField(max_length=100)
    class Meta:
        model = Meeting
        fields = ('cell', 'member', 'attendee_list')
        # widgets =
        #     'attendees': forms.CheckboxSelectMultiple()
        # }
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        #sets fields initially to nothing for members
        self.fields['member'].queryset = Member.objects.none()
        if 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['member'].queryset = Member.objects.filter(cells=cell_id).order_by('member_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['member'].queryset = self.instance.cell.member_set.order_by('member_name')

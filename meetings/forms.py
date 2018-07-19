from django import forms
from meetings.models import Cell, Objective, Member, Meeting

# CELL_CHOICES = [
#     ('tim', 'TIM'),
#     ('crispr', 'CRISPR'),
#     ('lotus', 'Lotus'),
#     ]

#member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=cell.members)
class WorkReview(forms.Form):
    class Meta:
        model = Meeting
        fields = ('cell', 'member')
    file_loc = forms.CharField(max_length=100)
    val1 = forms.CheckboxSelectMultiple()
    val2 = forms.CheckboxSelectMultiple()
    val3 = forms.CheckboxSelectMultiple()

class MeetingForm(forms.ModelForm):

    class Meta:
        model = Meeting
        fields = ('cell', 'member')
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

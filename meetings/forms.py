from django import forms
from meetings.models import Cell, Objective, Member, Meeting

# CELL_CHOICES = [
#     ('tim', 'TIM'),
#     ('crispr', 'CRISPR'),
#     ('lotus', 'Lotus'),
#     ]

#member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=cell.members)
class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ('cell', 'member')


    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        #sets fields initially to nothing for members
        self.fields['member'].queryset = Member.objects.none()
        print(self.data)
        if 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['member'].queryset = Member.objects.filter(cells=cell_id).order_by('member_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['member'].queryset = self.instance.cell.member_set.order_by('member_name')

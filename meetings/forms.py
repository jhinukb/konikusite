from django import forms
from meetings.models import Cell, Objective, Member, CellForm

CELL_CHOICES = [
    ('tim', 'TIM'),
    ('crispr', 'CRISPR'),
    ('lotus', 'Lotus'),
    ]

#member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=cell.members)
class CellForm(forms.ModelForm):
    class Meta:
        model = CellForm
        fields = ('cell', 'member')
        member_name= forms.CharField(label='What is your Cell?', widget=forms.Select(choices=CELL_CHOICES))
        email= forms.EmailField()
        cell = forms.CharField(label='What is your Cell?', widget=forms.Select(choices=CELL_CHOICES))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['member'].queryset = Member.objects.none()

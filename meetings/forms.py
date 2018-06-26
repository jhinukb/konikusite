from django import forms
from meetings.models import Cell, Objectives, Member

CELL_CHOICES = [
    ('tim', 'TIM'),
    ('crispr', 'CRISPR'),
    ('lotus', 'Lotus'),
    ]

class CellForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('cell', 'member_name')
        member_name= forms.CharField(label='What is your Cell?', widget=forms.Select(choices=CELL_CHOICES))
    #forms.CharField(max_length=100)
        email= forms.EmailField()
        cell = forms.CharField(label='What is your Cell?', widget=forms.Select(choices=CELL_CHOICES))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['member_name'].queryset = City.objects.none()

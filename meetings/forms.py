from django import forms
from meetings.models import Cell, Objectives, Member

CELL_CHOICES = [
    ('tim', 'TIM'),
    ('crispr', 'CRISPR'),
    ('lotus', 'Lotus'),
    ]

class CellForm(forms.ModelForm):
    class Meta:
        model = Cell
        fields = '__all__'
        cell_name= forms.CharField(max_length=100)
        email= forms.EmailField()
        cell = forms.CharField(label='What is your Cell?', widget=forms.Select(choices=CELL_CHOICES))

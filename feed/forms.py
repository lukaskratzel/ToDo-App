from django import forms
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['text', 'priority']

    text = forms.CharField(max_length=ToDo.text_max_length)
    priority = forms.ChoiceField(choices=ToDo.priority_choices, widget=forms.Select)

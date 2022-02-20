from cProfile import label
from django import forms

class MemoryForm(forms.Form):
    memory_name = forms.CharField(label='Memory name', max_length=100)
    memory_description = forms.TextInput()
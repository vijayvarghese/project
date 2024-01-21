from django import forms
from django.forms import CharField
from django.contrib.admin.widgets import AdminTextareaWidget
from .models import MyFormData

class MyForm(forms.ModelForm):
    # Add a rich text box field
    #rich_text_field = CharField(widget=AdminTextareaWidget)

    class Meta:
        model = MyFormData
        fields = ['input1', 'input2', 'rich_text_field']

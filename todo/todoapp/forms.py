from django import forms
#model forms

from django.forms import ModelForm
from .models import Todos


class TodoCreateForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()
    options=(("completed","completed"),
             ("notcompleted","notcompleted")
             )

    status=forms.ChoiceField(choices=options)
class TodoModelForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["task_name","user","status"]
from django import forms


#we have to create a form for creating todoapp


class TodoCreateForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()
    options=(("completed","completed"),
            ("notcompleted","notcompleted")
            )
    status=forms.ChoiceField(choices=options)
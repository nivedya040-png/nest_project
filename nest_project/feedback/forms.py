from django import forms
from .models import feedback

class feedbackform(forms.ModelForm):

    class Meta:
        model = feedback
        fields = ['name', 'department', 'feedback_type', 'message']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })
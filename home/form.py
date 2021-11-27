from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class BlogFrom(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields= ["content"]
from dataclasses import fields
from django import forms
from demoapp.models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

class EditorForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model = Editor
        fields = '__all__'        


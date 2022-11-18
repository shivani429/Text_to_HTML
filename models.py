from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# from django.db.models import signals
# from django.dispatch import receiver

# Create your models here.


class Editor(models.Model):
    body = RichTextField(blank = True, null = True) 


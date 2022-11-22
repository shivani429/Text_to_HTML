from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import Editor    
from demoapp.forms import EditorForm
# from .models import Blog


#Text To HTML    
def editor(request):
    form = EditorForm() 
    return render(request,'editor.html',{'form':form})   
    

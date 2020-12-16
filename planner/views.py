from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Teaching_method, Skill, Clo, Ilo
from .forms import Step1Form, Step2Form, Step3Form

# Create your views here.
def index(request):
    return HttpResponse("App: Planner, development started")

def step1(request):
    form = Step1Form()
    
    return render(request, 'planner/step1.html', {'form': form})

def step2(request):
    form = Step2Form()
    
    aux_skill = request.POST.get("skill")
    aux_clo = request.POST.get("clo")
    aux_ilo = request.POST.get("ilo")
    
    context={
        'skill': aux_skill,
        'clo': aux_clo,
        'ilo': aux_ilo,
        'form': form,
    }
    
    return render(request, 'planner/step2.html', context)

def step3(request):
    form = Step3Form()
    
    aux_skill = request.POST.get("skill")
    aux_clo = request.POST.get("clo")
    aux_ilo = request.POST.get("ilo")
    aux_content = request.POST.get("content_description")
    aux_delivery_method = request.POST.get("content_delivery_method")
    aux_intended_use = request.POST.get("intended_content_use")
    
    context={
        'skill': aux_skill,
        'clo': aux_clo,
        'ilo': aux_ilo,
        'content': aux_content,
        'delivery_method': aux_delivery_method,
        'intended_use': aux_intended_use,
        'form': form,
    }
    
    return render(request, 'planner/step3.html', context)

def step4(request):
    
    aux_skill = request.POST.get("skill")
    aux_clo = request.POST.get("clo")
    aux_ilo = request.POST.get("ilo")
    aux_content = request.POST.get("content")
    aux_delivery_method = request.POST.get("delivery_method")
    aux_intended_use = request.POST.get("intended_use")
    aux_learning_activities = request.POST.get("learning_activities")
    aux_ideal_outcome = request.POST.get("ideal_outcome")
    
    context={
        'skill': aux_skill,
        'clo': aux_clo,
        'ilo': aux_ilo,
        'content': aux_content,
        'delivery_method': aux_delivery_method,
        'intended_use': aux_intended_use,
        'learning_activities': aux_learning_activities,
        'ideal_outcome': aux_ideal_outcome,
    }
    
    return render(request, 'planner/step4.html', context)

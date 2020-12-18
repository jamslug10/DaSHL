from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Teaching_method, Skill, Clo, Ilo, Content, Learning_activity
from .models import Ibs, Session_plan

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
    aux_teaching_method = request.POST.get("teaching_method")
    
    context={
        'skill': aux_skill,
        'clo': aux_clo,
        'ilo': aux_ilo,
        'teaching_method': aux_teaching_method,
        'form': form,
    }
    
    return render(request, 'planner/step2.html', context)

def step3(request):
    form = Step3Form()
    
    aux_skill = request.POST.get("skill")
    aux_clo = request.POST.get("clo")
    aux_ilo = request.POST.get("ilo")
    aux_teaching_method = request.POST.get("teaching_method")
    aux_content = request.POST.get("content_description")
    aux_delivery_method = request.POST.get("content_delivery_method")
    aux_intended_use = request.POST.get("intended_content_use")
    
    context={
        'skill': aux_skill,
        'clo': aux_clo,
        'ilo': aux_ilo,
        'teaching_method': aux_teaching_method,
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
    aux_teaching_method = request.POST.get("teaching_method")
    aux_content = request.POST.get("content")
    aux_delivery_method = request.POST.get("delivery_method")
    aux_intended_use = request.POST.get("intended_use")
    aux_learning_activities = request.POST.get("learning_activities")
    aux_ideal_outcome = request.POST.get("ideal_outcome")
    
    literal_teaching_method = Teaching_method.objects.get(id=aux_teaching_method)
    
    # before we present the session plan the user it must be stored on the database.
    # This process follows a number of steps:
    #     1. create the skill
    #     2. create the CLO
    #     3. create the ILO
    #     4. create the session_plan
    #     5. assign default values for the hybridlearning part
    
    user_skill = Skill(skill_name='competencia generada por usuario anonimo',
                       skill_description=aux_skill)
    user_skill.save()
    
    #if the operation ends as expected we can create a new clo passing the user_skill object
    #as the foreign key
    
    user_clo = Clo(skill=user_skill, clo_name='CLO generado por usuario anonimo',
                   clo_description=aux_clo)
    user_clo.save()
    
    #same as before, we are passing the user_clo object as the foreign key for the ilo
    
    user_ilo = Ilo(clo=user_clo, ilo_name='ILO generado por usuario anonimo',
                   ilo_description=aux_ilo)
    user_ilo.save()
    
    #now for the content part
    user_content = Content(content_name='Contenido generado por usuario anonimo',
                           content_description=aux_content,
                           content_url='#')
    user_content.save()
    
    #and the learning_activities
    user_learning_activity = Learning_activity(learning_activity_name='AA generada por u. anonimo',
                                               learning_activity_description = aux_learning_activities)
    user_learning_activity.save()
    
    default_ibs = Ibs.objects.get(id=3)
    
    #and finally, we're ready to create our session_plan, at least, the non hybrid specific part
    user_session_plan = Session_plan(teaching_method=literal_teaching_method,
                                     # clo=user_clo,
                                     # ilo=user_ilo,
                                     # content=user_content,
                                     # ibs=default_ibs,
                                     # learning_activity=user_learning_activity,
                                     session_plan_name='planeacion generada por u. anonimo',
                                     session_plan_content_delivery_method=aux_delivery_method,
                                     session_plan_intended_content_use=aux_intended_use,
                                     session_plan_feedback_detail='not defined',
                                     session_plan_participation_detail='not defined')
    user_session_plan.save()
    
    #Now we need to add the ManyToMany elements
    user_session_plan.clo.add(user_clo)
    user_session_plan.ilo.add(user_ilo)
    user_session_plan.content.add(user_content)
    user_session_plan.ibs.add(default_ibs)
    user_session_plan.learning_activity.add(user_learning_activity)
    
    context={
        'skill': aux_skill,
        'clo': aux_clo,
        'ilo': aux_ilo,
        # 'teaching_method': aux_teaching_method,
        'teaching_method': literal_teaching_method,
        'content': aux_content,
        'delivery_method': aux_delivery_method,
        'intended_use': aux_intended_use,
        'learning_activities': aux_learning_activities,
        'ideal_outcome': aux_ideal_outcome,
    }
    
    return render(request, 'planner/step4.html', context)

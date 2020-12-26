from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.index, name='index'),
    path('step1/', views.step1, name='step1'),
    path('step2/', views.step2, name='step2'),
    path('step3/', views.step3, name='step3'),
    path('step4/', views.step4, name='step4'),
    path('step5/', views.step5, name='step5'),
    path('step6/', views.step6, name='step6'),
    path('step7/', views.step7, name='step7'),
    path('step8/', views.step8, name='step8'),
    path('step9/', views.step9, name='step9'),
    path('step10/', views.step10, name='step10'),
    path('step11/', views.step11, name='step11'),
    path('step12/', views.step12, name='step12'),
    path('step13/', views.step13, name='step13'),
]

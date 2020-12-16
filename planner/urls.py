from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.index, name='index'),
    path('step1/', views.step1, name='step1'),
    path('step2/', views.step2, name='step2'),
    path('step3/', views.step3, name='step3'),
    path('step4/', views.step4, name='step4'),
]

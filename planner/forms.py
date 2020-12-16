from django import forms
from .models import Teaching_method

class Step1Form(forms.Form):
    skill = forms.CharField(label="Competencia asociada al curso",
                            max_length = 255)
    clo = forms.CharField(label="Resultado Esperado de Aprendizaje para el Curso (CLO)",
                          widget=forms.Textarea)
    ilo = forms.CharField(label="Resultado Esperado de Aprendizaje para la Sesión (ILO)",
                          widget=forms.Textarea)
    
    TEACHING_METHOD_CHOICES = [(teaching_method.id, teaching_method.teaching_method_name) 
                   for teaching_method in Teaching_method.objects.all()]
    
    teaching_method = forms.ChoiceField(label="Método de Enseñanza", widget=forms.Select,
                                        choices=TEACHING_METHOD_CHOICES)
    
class Step2Form(forms.Form):
    content_description = forms.CharField(label="¿Cuál es el contenido que desea presentar\
                                           en esta sesión?", widget=forms.Textarea)
    content_delivery_method = forms.CharField(label="¿De qué manera desea que los estudiantes\
                                               accedan a este contenido?", widget=forms.Textarea)
    intended_content_use = forms.CharField(label="¿Qué espera que los estudiantes hagan con \
                                           esta nueva información?", widget=forms.Textarea)
    
class Step3Form(forms.Form):
    learning_activities = forms.CharField(label="¿Qué actividades de aprendizaje desea incluir en \
                                         esta sesión, con el ánimo de determinar si los estudiantes \
                                         han alcanzado los ILOs?", widget=forms.Textarea)
    ideal_outcome = forms.CharField(label="¿Cuál sería el resultado ideal que le gustaría encontrar \
                                   al evaluar estas actividades?", widget=forms.Textarea)
    
from django import forms
from .models import Teaching_method, Platform, Ibs, Group_configuration

class Step1Form(forms.Form):
    skill = forms.CharField(label="Competencia asociada al curso",
                            max_length = 255,
                            widget=forms.TextInput(attrs={"size":53}))
    clo = forms.CharField(label="Resultado Esperado de Aprendizaje para el Curso (CLO)",
                          widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    ilo = forms.CharField(label="Resultado Esperado de Aprendizaje para la Sesión (ILO)",
                          widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    
    TEACHING_METHOD_CHOICES = [(teaching_method.id, teaching_method.teaching_method_name) 
                   for teaching_method in Teaching_method.objects.all()]
    
    teaching_method = forms.ChoiceField(label="Método de Enseñanza", widget=forms.Select,
                                        choices=TEACHING_METHOD_CHOICES)
    
class Step2Form(forms.Form):
    content_description = forms.CharField(label="¿Cuál es el contenido que desea presentar\
                                           en esta sesión?",
                                        widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    content_delivery_method = forms.CharField(label="¿De qué manera desea que los estudiantes\
                                               accedan a este contenido?",
                                        widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    intended_content_use = forms.CharField(label="¿Qué espera que los estudiantes hagan con \
                                           esta nueva información?",
                                        widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    
class Step3Form(forms.Form):
    learning_activities = forms.CharField(label="¿Qué actividades de aprendizaje desea incluir en \
                                         esta sesión?",
                                        widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    ideal_outcome = forms.CharField(label="¿Cuál sería el resultado ideal al evaluar estas \
                                    actividades?",
                                    widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    
class Step5Form(forms.Form):
    AVAILABLE_PLATFORM_CHOICES = [(platform.id, platform.platform_name)
        for platform in Platform.objects.all()]
    
    platform = forms.ChoiceField(label="¿Qué plataforma utilizan los estudiantes \
                                 para conectarse remotamente al salón de clases?",
    widget=forms.RadioSelect, choices = AVAILABLE_PLATFORM_CHOICES)
    
class Step6Form(forms.Form):
	AVAILABLE_IBS_VISUAL_CHOICES = [(ibs.id, ibs.ibs_name)
		for ibs in Ibs.objects.filter(ibs_type="V", ibs_com_direction="R")] 
	
	ibs_visual_remote = forms.ChoiceField(label="¿De qué manera se visualizan, en su salón de \
                                          clases, los estudiantes que se conectan remotamente?",
    widget=forms.RadioSelect, choices = AVAILABLE_IBS_VISUAL_CHOICES)
    
class Step7Form(forms.Form):
	AVAILABLE_IBS_AUDIO_CHOICES = [(ibs.id, ibs.ibs_name)
		for ibs in Ibs.objects.filter(ibs_type="A", ibs_com_direction="R")] 
	
	ibs_audio_remote = forms.ChoiceField(label="¿De qué manera se escuchan, en su salón de \
                                         clases, los estudiantes que se conectan remotamente?",
    widget=forms.RadioSelect, choices = AVAILABLE_IBS_AUDIO_CHOICES)

class Step8Form(forms.Form):
	AVAILABLE_IBS_VISUAL_CHOICES = [(ibs.id, ibs.ibs_name)
		for ibs in Ibs.objects.filter(ibs_type="V", ibs_com_direction="P")] 
	
	ibs_visual_face2face = forms.ChoiceField(label="¿De qué manera se visualiza, por parte de los \
                                          estudiantes que se conectan remotamente, lo que ocurre \
                                          en el salón de clase así como a quienes asisten de manera \
                                          presencial a ella?",
    widget=forms.RadioSelect, choices = AVAILABLE_IBS_VISUAL_CHOICES)
    
class Step9Form(forms.Form):
	AVAILABLE_IBS_AUDIO_CHOICES = [(ibs.id, ibs.ibs_name)
		for ibs in Ibs.objects.filter(ibs_type="A", ibs_com_direction="P")] 
	
	ibs_audio_face2face = forms.ChoiceField(label="¿De qué manera se transmite el audio, a los \
                                          estudiantes que se conectan remotamente, de lo que ocurre \
                                          en el salón de clase así como las intervenciones que se \
                                          dan de manera presencial?",
    widget=forms.RadioSelect, choices = AVAILABLE_IBS_AUDIO_CHOICES)
    
class Step10Form(forms.Form):
	AVAILABLE_GROUP_CONFIGURATION = [(gc.id, gc.group_configuration_description)
		for gc in Group_configuration.objects.all()] 
	
	group_configuration = forms.ChoiceField(label="Al momento de plantear una actividad de \
                                            aprendizaje grupal, usted prefiere:",
    widget=forms.RadioSelect, choices = AVAILABLE_GROUP_CONFIGURATION)
    
class Step11Form(forms.Form):
    feedback_detail = forms.CharField(label="¿Cómo garantiza que la realimentación que reciben \
                                      los estudiantes que asisten presencialmente y aquellos que \
                                      se conenctan de manera remota sea la misma?",
                                        widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    
class Step12Form(forms.Form):
    participation_detail = forms.CharField(label="¿Cómo garantiza que los estudiantes que se \
                                           conectan remotamente y aquellos que asisten de manera \
                                           presencial, cuenten con las mismas oportunidades para \
                                           participar?",
                                        widget=forms.Textarea(attrs={"rows":5, "cols":26}))
    
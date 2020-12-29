from django.db import models

# Create your models here.
class Skill(models.Model):
    SKILL_TYPE_CHOICES = [
        ('SOFT','Soft (generic) Skill'),
        ('HARD', 'Hard (specific) Skill'),
        ] 
    skill_name = models.CharField(max_length=200)
    skill_type = models.CharField(
        max_length=4,
        choices=SKILL_TYPE_CHOICES,
        default='HARD',
        )
    skill_description = models.TextField()
    
    def __str__(self):
        return self.skill_name
    
class Clo(models.Model):
    SKILL_DEVELOPMENT_LEVELS = [
        ('UI','Unconscious Incompetence'),
        ('CI','Conscious Incompetence'),
        ('CC','Conscious Competence'),
        ('UC', 'Unconscious Competence'),
    ]
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    clo_name = models.CharField(max_length=200)
    clo_description = models.TextField()
    skill_development_level = models.CharField(
        max_length=2,
        choices=SKILL_DEVELOPMENT_LEVELS,
        default='UI',
    )
    
    def __str__(self):
        return self.clo_name
    
class Ilo(models.Model):
    clo = models.ForeignKey(Clo, on_delete=models.CASCADE)
    ilo_name = models.CharField(max_length=200)
    ilo_description = models.TextField()
    
    def __str__(self):
        return self.ilo_name
    
class Teaching_method(models.Model):
    teaching_method_name = models.CharField(max_length=200)
    teaching_method_description = models.TextField()
    teaching_method_suggested_scenario = models.TextField()
    
    def __str__(self):
        return self.teaching_method_name
    
class Content(models.Model):
    content_name = models.CharField(max_length=200)
    content_description = models.TextField()
    content_url = models.CharField(max_length=255)
    
    def __str__(self):
        return self.content_name

class Learning_activity(models.Model):
    learning_activity_name = models.CharField(max_length=200)
    learning_activity_description = models.TextField()
    
    def __str__(self):
        return self.learning_activity_name
    
class Group_configuration(models.Model):
    group_configuration_name = models.CharField(max_length=200)
    group_configuration_description = models.TextField()
    
    def __str__(self):
        return self.group_configuration_name
    
class Ibs(models.Model):
    IBS_TYPE = [
        ('A','Audio'),
        ('V','Visual'),
    ]
    IBS_COM_DIRECTION = [
        ('P','Desde los estudiantes que asisten presencialmente'),
        ('R','Desde los estudiantes que se conectan de manera remota'),
    ]
    ibs_name = models.CharField(max_length=200)
    ibs_description = models.TextField()
    ibs_type = models.CharField(
        max_length=1,
        choices=IBS_TYPE,
        default='A',
        )
    ibs_com_direction = models.CharField(
        max_length=1,
        choices=IBS_COM_DIRECTION,
        default='P',
    )
    
    def __str__(self):
        return self.ibs_name
    
class Platform(models.Model):
    platform_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.platform_name
    
class Session_plan(models.Model):
    teaching_method = models.ForeignKey(Teaching_method, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, default=1)
    group_configuration = models.ForeignKey(Group_configuration, on_delete=models.CASCADE, default=1)
    clo = models.ManyToManyField(Clo)
    ilo = models.ManyToManyField(Ilo)
    content = models.ManyToManyField(Content)
    ibs = models.ManyToManyField(Ibs)
    learning_activity = models.ManyToManyField(Learning_activity)
    session_plan_name = models.CharField(max_length=200, default='ingrese un nombre')
    session_plan_content_delivery_method = models.TextField()
    session_plan_intended_content_use = models.TextField()
    session_plan_feedback_detail = models.TextField()
    session_plan_participation_detail = models.TextField()
    
    def __str__(self):
        return self.session_plan_name
    
class Recommendation(models.Model):
    teaching_method = models.ForeignKey(Teaching_method, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    ibs = models.ForeignKey(Ibs, on_delete=models.CASCADE)
    group_configuration = models.ForeignKey(Group_configuration, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    recommendation_title = models.CharField(max_length=200)
    recommendation_body = models.TextField()
    
    def __str__(self):
        return self.recommendation_title
from django.contrib import admin

from .models import Skill, Clo, Ilo, Content, Group_configuration, Ibs, Learning_activity
from .models import Platform, Teaching_method, Session_plan, Recommendation

# Register your models here.
admin.site.register(Skill)
admin.site.register(Clo)
admin.site.register(Ilo)
admin.site.register(Content)
admin.site.register(Group_configuration)
admin.site.register(Ibs)
admin.site.register(Learning_activity)
admin.site.register(Platform)
admin.site.register(Teaching_method)
admin.site.register(Session_plan)
admin.site.register(Recommendation)

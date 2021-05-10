from django.contrib import admin

# Register your models here.
from .models import Task, HealthBody,SocialRelationship,Travel, SchoolWork,Nature,ABC

admin.site.register(Task)
admin.site.register(HealthBody)
admin.site.register(SocialRelationship)
admin.site.register(Travel)
admin.site.register(SchoolWork)
admin.site.register(Nature)
admin.site.register(ABC)
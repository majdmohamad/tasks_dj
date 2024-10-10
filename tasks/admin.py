from django.contrib import admin
from .models import Team,Task,Comment,Notification
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Notification)

# Register your models here.

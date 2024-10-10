from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User)
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField()
    assigned_to=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,choices=[('To Do','To Do'),('In Progress','In Progress'),('Done','Done')])
    due_date=models.DateField()
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'Comment by {self.user.username} on {self.task.title}'

class Notification(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.message
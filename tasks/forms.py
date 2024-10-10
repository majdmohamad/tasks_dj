from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models import Team,Task,Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','description','members']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','assigned_to','team','status','due_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']

class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','password']

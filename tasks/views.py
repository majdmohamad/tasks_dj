from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from .forms import RegisterForm,TeamForm,TaskForm,CommentForm,LoginForm
from .models import Task,Notification,Team
from django.contrib.auth.decorators import login_required


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home_page')
    else:
        form = RegisterForm()
    
    return render(request,'tasks/register.html',{'form':form,'current_page':'register'})

def home_page(request):
    team = Team.objects.all()
    tasks=Task.objects.all()
    members_performance={}
    for member in team:
        copleted_tasks=tasks.filter(status='Done').count()
        members_performance[member.name]=copleted_tasks
    return render(request,'tasks/home_page.html',{'current_page':'home_page','team':team,'members_performance':members_performance})

def logout_user(request):
    logout(request)
    return render(request,'tasks/logout.html',{'current_page':'logout'})

def login_user(request):
    if request.method=='POST':
        form=LoginForm()
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            messages.warning(request,'Tere is an error in the username or password')
    else:
        form=LoginForm()
    return render(request,'tasks/login.html',{'form':form,'current_page':'login'})

def create_team_view(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team =form.save(commit=False)
            team.save()
            team.members.add(request.user)
            return redirect('home_page')
    else:
        form = TeamForm()
        

    return render(request,'tasks/create_team.html',{'form':form})

def create_task_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task=form.save()
            Notification.objects.create(user=task.assigned_to,message=f'You have been assigned a new task: {task.title}')
            return redirect('home_page')
    else:
        form=TaskForm()

    return render(request,'tasks/create_task.html',{'form':form})

def task_list_view(request):
    tasks=Task.objects.all()
    return render(request,'tasks/task_list.html',{'tasks':tasks,'current_page':'task_list'})

def task_detail_view(request,task_id):
    task=get_object_or_404(Task,pk=task_id)
    comments=task.comments.all()
    
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment= form.save(commit=False)
            comment.task = task
            comment.user=request.user
            comment.save()
            return redirect('detail',task_id)
    else:
        form=CommentForm()

    return render(request,'tasks/task_detail.html',{'task':task,'comments':comments,"form":form,'task':task})

def notification_view(request):
    notifications=Notification.objects.filter(user=request.user,is_read=False) 

    return render(request,'tasks/notifications.html',{'notifications':notifications})


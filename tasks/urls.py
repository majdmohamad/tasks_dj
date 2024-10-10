from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('',views.home_page,name='home_page'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('create_team/',views.create_team_view,name='create_team'),
    path('create_task/',views.create_task_view,name='create_task'),
    path('task_list/',views.task_list_view,name='task_list'),
    path('detail/<int:task_id>/',views.task_detail_view,name='detail'),
    path('notifications/',views.notification_view,name='notifications'),
]

from django.urls import path
from .views import TaskListView,TaskCreateView,CategoryCreateView,CompletedTaskListView,RemainingTaskListView,TaskDetailView,TaskDeleteView,ToggleCompleteView,delete_task,remove_task
urlpatterns = [
    path('task_list/',TaskListView.as_view(),name='task_list'),
    path('add_task/',TaskCreateView.as_view(),name='add_task'),
    path('add_category/',CategoryCreateView.as_view(),name='add_category'),
    path('completed',CompletedTaskListView.as_view(), name='completed'),
    path('remaining',RemainingTaskListView.as_view(), name='remaining'),
    path('toggle_complete/<int:task_id>',ToggleCompleteView.as_view(), name='toggle_complete'),
    path('detail/<int:task_id>',TaskDetailView.as_view(), name='task_detail'),
    path('delete/<int:task_id>',delete_task, name='delete'),
    path('remove_task/<int:task_id>',remove_task, name='remove_task'),
]

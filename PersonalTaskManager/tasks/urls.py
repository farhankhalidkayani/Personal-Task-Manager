from django.urls import path
from . import views


app_name = "tasks"
urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.add_task, name="add_task"),
    path("update/<int:id>", views.update_task, name="update_task"),
    path("delete/<int:id>", views.delete_task, name="delete_task"),
]

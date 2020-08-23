from django.urls import path
from . import views

urlpatterns = [
	path('todos/', views.TodoListCreat.as_view()),
	path('todos/<int:pk>/', views.TodoRetriveUpdateDestroy.as_view()),

    path('todos/completed/', views.TodoCompleted.as_view()),
]

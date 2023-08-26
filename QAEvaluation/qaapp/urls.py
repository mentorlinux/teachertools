from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_question, name='submit_question'),
    path('evaluate/<int:question_id>/', views.evaluate_answer, name='evaluate'),
]

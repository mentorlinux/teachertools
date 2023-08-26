from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    question_text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    evaluation = models.CharField(max_length=100)

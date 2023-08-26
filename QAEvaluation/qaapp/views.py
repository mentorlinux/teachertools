from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Question, Answer

def submit_question(request):
    if request.method == 'POST':
        question_text = request.POST['question_text']
        question = Question.objects.create(question_text=question_text)
        return redirect('evaluate', question_id=question.id)
    return render(request, 'qaapp/submit_question.html')

def evaluate_answer(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        answer_text = request.POST['answer_text']
        evaluation = perform_evaluation(answer_text)  # Implement your evaluation logic
        Answer.objects.create(question=question, answer_text=answer_text, evaluation=evaluation)
        return redirect('submit_question')
    return render(request, 'qaapp/evaluate_answer.html', {'question': question})

def perform_evaluation(answer_text, question_id):
    # write code below to check answer_text with chatgpt for the respective question
    # if answer_text is positive, return "Positive"
    return "Positive"  # Replace with actual evaluation result

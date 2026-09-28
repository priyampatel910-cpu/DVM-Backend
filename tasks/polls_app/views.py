from django.shortcuts import render
from .models import *

def index(request):
    questions = Question.objects.all()
    return render(request, "index.html",{
        "questions": questions
    })

def  details(request, question_id):
    question = Question.objects.get(id = question_id)
    return render(request, "details.html",{
        "question": question
    })

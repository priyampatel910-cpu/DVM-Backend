from django.shortcuts import render
from .models import *

def index(request):
    questions = Question.objects.all()
    return render(request, "index.html",{
        "questions": questions
    })

from django.shortcuts import get_object_or_404, render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    questions = Question.objects.all()
    return render(request, "index.html",{
        "questions": questions
    })


def details(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        choice = get_object_or_404(question.choice_set, id=choice_id)
        choice.votes += 1
        choice.save()
        return redirect("polls:results", question_id=question.id)

    return render(request, "details.html", {
        "question": question
    })

def results(request, question_id):

    question = get_object_or_404(Question, id=question_id)

    return render(request, "results.html", {
        "question": question
    })

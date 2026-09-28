from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    questions = Question.objects.all()
    return render(request, "index.html",{
        "questions": questions
    })

def details(request, question_id):
    question = Question.objects.get(id = question_id)
    return render(request, "details.html",{
        "question": question
    })

def vote(request, question_id):
    question = Question.objects.get(pk = question_id)
    try:
        selected_choice = question.choices.get(pk = request.POST["choice"])

    except(KeyError, Choice.DoesNotExist):
        return render(request, "details.html", {
            "question": question,
            "error_message": "You did not select a vaild response",
        })

    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id)))

from django.shortcuts import get_object_or_404, render, redirect
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
        choice = get_object_or_404(question.choices, id=choice_id)
        choice.votes += 1
        choice.save()
        return redirect("polls:results", question_id=question.id)

    return render(request, "details.html", {
        "question": question,
        "choices": question.choices.all()
    })

def results(request, question_id):

    question = get_object_or_404(Question, id=question_id)

    return render(request, "result.html", {
        "question": question,
        "choices": question.choices.all()
    })


# This is the view ofthe new feature, which is adding a feature for user to add a poll of their own to the list

def add_poll(request):
    if request.method == "POST":
        question_text = request.POST.get("question")
        choice1 = request.POST.get("choice1")
        choice2 = request.POST.get("choice2")
        choice3 = request.POST.get("choice3")

        question = Question.objects.create(question_text=question_text)

        question.choices.create(choice_text=choice1)

        question.choices.create(choice_text=choice2)

        question.choices.create(choice_text=choice3)

        return redirect("polls:index")

    return render(request,"add_poll.html")

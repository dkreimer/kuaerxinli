from django.shortcuts import render, get_object_or_404
from .models import Quiz

def take(request,quiz_id):
    return render(request, 'quiz/take.html', {'quiz':get_object_or_404(Quiz,pk=quiz_id)})

def submit(request,quiz_id):
    return render(request,'quiz/submit.html',{})

def results(request,quiz_id):
    return render(request,'quiz/results.html',{})

def index(request):
    return render(request,'quiz/index.html',{'quizzes':Quiz.objects.all()})


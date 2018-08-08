from django.shortcuts import render

def take(request):
    return render(request, 'quiz/take.html', {})


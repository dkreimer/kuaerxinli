from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Choice, Profile
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def take(request,quiz_id):
    #only logged in users should be able to view
    return render(request, 'quiz/take.html', {'quiz':get_object_or_404(Quiz,pk=quiz_id)})

def submit(request,quiz_id):
    #only logged in users should be able to view
    quiz = get_object_or_404(Quiz,pk=quiz_id)
    user = request.user
    for question in quiz.question_set.all():
        p = question.result
        try:
            selected = question.choice_set.get(pk=request.POST['choice-q'+str(question.id)])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay voting form
            return render(request,'quiz/take.html',{
                'quiz': quiz, 
                'error_message': 'You didn\'t select a choice'
                })
        else:
            p.tally += selected.points
            p.save()
            if user.score_set.get(result = p): #double check syntax
                #(get the ser of user scores and see if any of them correspond to p)
                s = user.score_set.get(result = p) #generalize this line/define variable earlier
                    #like can i use getobjector404 here?
                s.score += selected.points
                s.save()
            else: #create new score
                s = Score.create(user = user, result = p, score = selected.points)
                s.save()
            # check if user has a score object associated to this result
            # if yes: add the points to the score
            # if no: create score object and add points to score
    return HttpResponseRedirect(reverse('quiz:results',args=(quiz.id,)))

    

'''
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''

def results(request,quiz_id):
    #only logged in users should be able to view
    return render(request,'quiz/results.html',{'quiz': get_object_or_404(Quiz,pk=quiz_id)})

def index(request):
    #Only show to logged in users
    return render(request,'quiz/index.html',{'quizzes':Quiz.objects.all()})


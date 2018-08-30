from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Choice, Result, Score
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def take(request,quiz_id):
    #only logged in users should be able to view
    return render(request, 'quiz/take.html', {'quiz':get_object_or_404(Quiz,pk=quiz_id)})

@login_required
def submit(request,quiz_id):
    #only logged in users should be able to view
    quiz = get_object_or_404(Quiz,pk=quiz_id)
    user = request.user
    quiz_results = quiz.result_set.all()
    if quiz.been_taken(user):
        for r in quiz_results:
            for score in user.score_set.filter(result = r):
                score.reset()
    for question in quiz.question_set.all():
        results = question.result.all()
        try:
            selected = question.choice_set.get(pk=request.POST['choice-q'+str(question.id)])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay voting form
            return render(request,'quiz/take.html',{
                'quiz': quiz, 
                'error_message': 'You didn\'t select a choice'
                })
        else:
            for result in results:
                # result.raw_so_far += selected.points
                # print (result.raw_so_far)
                # result.save()
                s = Score.objects.get_or_create(result = result, user = user)[0]
                s.score += selected.points
                s.save()
    
    for r in quiz_results:
        user_score = r.score_set.filter(user = user)[0].process_score()
        r.raw_so_far += user_score
        r.save()
        r.users_tally += 1
        r.save()
        r.avg = r.raw_so_far / r.users_tally
        r.save()

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

@login_required
def results(request,quiz_id):
    #only logged in users should be able to view
    quiz = get_object_or_404(Quiz,pk=quiz_id)
    user = request.user
    return render(request,'quiz/results.html',{'quiz': quiz,})

def index(request):
    return render(request,'quiz/index.html',{'quizzes':Quiz.objects.all()})


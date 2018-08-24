from django.db import models
from django.conf import settings

class Quiz(models.Model):
    ''' 
    This is the model for a single quiz/questionnaire.
    '''
    STATUS_CHOICES = (
		(1, ('Draft')),
		(2, ('Public')),
		(3, ('Close')),
        )
    title = models.CharField(max_length=100,
                            default='',
                            verbose_name="Title")

    desc = models.TextField(default='',
                            verbose_name= 'Description')

    status = models.IntegerField(choices = STATUS_CHOICES, 
                                default= 1,
                                verbose_name= 'Status')

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title

class Result(models.Model):
    '''
    Model for a possible Result that is being measured in the quiz. For example,
    "Depression" would be a Result, and the quiz would tally how many points have globally
    been scored that fall under the "Depression" Result. "Total" is also an example of a Result.
    '''
    name = models.CharField(max_length=100,
                            default='',
                            verbose_name= 'Name')

    desc = models.TextField(default='',
                            verbose_name= 'Description')

    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE, 
                            blank = True, 
                            null=True,
                            verbose_name = 'Quiz')

    tally = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    '''
    Model for a question.
    '''
    #QUESTION_TYPES = (('Scale','Scale'))

    txt = models.CharField(max_length=200,
                            verbose_name='Text')

    quiz = models.ForeignKey(Quiz, 
                            on_delete=models.CASCADE, 
                            blank = True, 
                            null = True,
                            verbose_name = 'Quiz')

    result = models.ManyToManyField(Result, 
                                blank= True, 
                                verbose_name = 'Result')
    #Qtype = models.CharField(choices = QUESTION_TYPES, default = 'Scale')

    def __str__(self):
        return self.txt
'''
    def make_scale(self,labels=['Not at all','A little','Moderately','Quite a bit','Extremely']):
        idx = 0
        for lb in labels:
            self.choice_set.create(txt=label, 
                                 points= idx,
                                 question = self)
            idx+=1
'''

class ScaleQuestion(Question):
    class Meta:
        proxy = True
''' WIP --- Making a Question whose choices go from Not at all (0 points) to Extremely (4 pts)
    def setup(self):
        SCALE = [('Not at all', 0),
             ('A little', 1),
             ('Moderately', 2),
             ('Quite a bit', 3),
             ('Extremely', 4)]
        for opt in SCALE:
            choice_set.create(txt=opt[1],points=opt[2],question=self)
            '''
    

class Choice(models.Model):
    '''
    Model for a single choice (of a question with multiple choices).
    '''
    txt = models.CharField(max_length=100,
                            verbose_name = 'Text')

    points = models.IntegerField(verbose_name='Points',
                                default=0)

    question = models.ManyToManyField(Question, 
                                        blank = True, 
                                        verbose_name = 'Questions')

    def __str__(self):
        return self.txt

class Score(models.Model):
    '''
    Bridges the user with the result. Holds a particular user's numerical score for a
    particular Result.
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete = models.CASCADE)
    result = models.ForeignKey(Result,
                              on_delete = models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.score

    def reset(self):
        self.score = 0




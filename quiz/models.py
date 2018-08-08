from django.db import models

class Quiz(models.Model):
    ''' 
    This is the model for a single quiz/questionnaire.
    '''
    title = models.CharField(max_length=100,default='')
    desc = models.TextField(default='')

    def __str__(self):
        return self.title

class Profile(models.Model):
    '''
    Model for a possible profile that is being measured in the quiz. For example,
    "Depression" would be a profile, and the quiz would tally how many points the user scored
    that fall under the "Depression" profile. 
    '''
    name = models.CharField(max_length=100,default='')
    desc = models.TextField(default='')
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    tally = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model):
    '''
    Model for a question.
    '''
    txt = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

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
    txt = models.CharField(max_length=100)
    points = models.IntegerField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.txt




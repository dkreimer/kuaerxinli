from django.db import models

class Quiz(models.Model):
    ''' 
    This is the model for a single quiz/questionnaire.
    '''
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    '''
    Model for a possible profile that is being measured in the quiz. For example,
    "Depression" would be a profile, and the quiz would tally how many points the user scored
    that fall under the "Depression" profile. 
    '''
    name = models.CharField(max_length=100)
    desc = models.TextField()
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

class Choice(models.Model):
    '''
    Model for a single choice (of a question with multiple choices).
    '''
    txt = models.CharField(max_length=100)
    points = models.IntegerField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.txt




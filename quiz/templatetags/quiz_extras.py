from django import template

register = template.Library()

@register.filter
def user_score(score_set,user):
    '''Gets a particular user's score from a set of scores related to a specific result'''
    return score_set.get(user = user)

@register.simple_tag
def taken_by_user(quiz,user):
    return quiz.been_taken(user)
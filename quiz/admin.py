from django.contrib import admin

from .models import Quiz, Question, Choice, Result

class ChoicesInline(admin.TabularInline):
    model = Choice.question.through

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline]

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline]
    exclude = ('choices',)

class ResultInLine(admin.StackedInline):
    model = Result
    extra = 1
    readonly_fields = ['users_tally','raw_so_far','avg']

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    radio_fields = {"status": True}
    inlines = [ResultInLine,QuestionInLine]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
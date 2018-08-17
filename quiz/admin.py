from django.contrib import admin

from .models import Quiz, Question, Choice, Profile

class ChoicesInline(admin.TabularInline):
    model = Choice.questions.through

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline]

class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoicesInline]
    exclude = ('choices',)

class ProfileInLine(admin.StackedInline):
    model = Profile
    extra = 1

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    radio_fields = {"status": True}
    inlines = [ProfileInLine,QuestionInLine]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
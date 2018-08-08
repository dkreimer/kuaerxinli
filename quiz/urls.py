from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:quiz_id>/',views.take,name='detail'),
    path('<int:quiz_id>/submit/',views.submit,name='submit'),
    path('<int:quiz_id>/results/',views.results,name="results"),
]
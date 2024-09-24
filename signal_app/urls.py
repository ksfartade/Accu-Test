from django.urls import path
from .views import question1, question2, question3


urlpatterns = [
    path('question1/', question1),
    path('question2/', question2),
    path('question3/', question3)
]
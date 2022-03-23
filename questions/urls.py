# from .api import QuestionViewSet, OptionsViewSet, KeywordViewSet, MatchViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('questions', QuestionViewSet, 'questions')
# router.register('options', OptionsViewSet, 'options')
# router.register('keyword', KeywordViewSet, 'keywords')
# router.register('match', MatchViewSet, 'matches')

# urlpatterns = []

# urlpatterns += router.urls


from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('create', createQuestionsView.as_view(), name="create-question"),
	path('<int:ques_id>', GetQuestionView.as_view(), name="get-question"),
    path('retrieve', RetreiveQuestionView.as_view(), name="retrieve-question")
]
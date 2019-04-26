from django.urls import path
from . import views
app_name = "forum"

urlpatterns = [path('questions/', views.QuestionList.as_view(), name='questions'),
               path('questions/<pk>/', views.QuestionDetail.as_view(), name='detail'),
               path('questions/<pk>/answer/<answer_pk>/', views.AnswerDetail.as_view(), name='answer'),
               ]

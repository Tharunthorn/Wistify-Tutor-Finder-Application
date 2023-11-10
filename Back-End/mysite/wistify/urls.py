from django.urls import path
from . import views

urlpatterns = [
    path('', views.getLearner),
    path('signup/', views.LearnerSignUp.as_view()),
]
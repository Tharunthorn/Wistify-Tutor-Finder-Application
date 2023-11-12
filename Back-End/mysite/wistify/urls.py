from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='getlearner/')),
    path('getlearner/', views.GetLearner.as_view()),
    path('signup/', views.LearnerSignUp.as_view()),
    path('login/', views.LearnerLogIn.as_view()),
]
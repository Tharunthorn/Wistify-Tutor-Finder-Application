from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('learners/', views.GetLearner.as_view(), name='get_learners'),
    path('learners/signup/', views.LearnerSignUp.as_view(), name='learner_signup'),
    path('tutors/', views.GetTutor.as_view(), name='get_tutors'),
    path('tutors/signup/', views.TutorSignUp.as_view(), name='tutor_signup'),
    path('login/', views.LogIn.as_view(), name='tutor_login'),
]
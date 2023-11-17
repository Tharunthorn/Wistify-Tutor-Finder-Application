from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='get_learner/')),
    path('get_learner/', views.GetLearner.as_view()),
    path('get_tutor/', views.GetTutor.as_view()),
    path('get_rating/', views.GetRating.as_view()),
    path('get_tag/', views.GetTag.as_view()),
    path('get_video/', views.GetVideo.as_view()),
    path('learner_sign_up/', views.LearnerSignUp.as_view()),
    path('tutor_sign_up/', views.TutorSignUp.as_view()),
    path('log_in/', views.LogIn.as_view()),
    path('rating/', views.UserRating.as_view()),
    path('add_tag/', views.AddTag.as_view()),
    path('add_video/', views.AddVideo.as_view()),
]
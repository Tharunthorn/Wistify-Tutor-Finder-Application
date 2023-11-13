from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Learner, Tutor
from .serializers import LearnerSerializer, TutorSerializer, LogInSerializer, SignUpSerializer
from .authentication import create_access_token, create_refresh_token
from django.contrib.auth.hashers import check_password


class GetLearner(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        learners = Learner.objects.all()
        serializer = LearnerSerializer(learners, many=True)
        return Response(serializer.data)


class GetTutor(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response(serializer.data)


class LearnerSignUp(APIView):
    def post(self, request):
        user_serializer = SignUpSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()
        learner = Learner.objects.create(user=user)
        learner_serializer = LearnerSerializer(learner)

        return Response(learner_serializer.data, status=status.HTTP_201_CREATED)


class TutorSignUp(APIView):
    def post(self, request):
        user_serializer = SignUpSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()
        tutor = Tutor.objects.create(user=user)
        tutor_serializer = TutorSerializer(tutor)

        return Response(tutor_serializer.data, status=status.HTTP_201_CREATED)


class LogIn(APIView):
    def post(self, request):
        login_serializer = LogInSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)

        email = login_serializer.validated_data['email']
        password = login_serializer.validated_data['password']

        try:
            learner = Learner.objects.get(user__email=email)
            is_learner = True
        except Learner.DoesNotExist:
            try:
                tutor = Tutor.objects.get(user__email=email)
                is_learner = False
            except Tutor.DoesNotExist:
                raise APIException('Incorrect Email or Password', status_code=status.HTTP_401_UNAUTHORIZED)

        user = learner.user if is_learner else tutor.user
        correct_password = check_password(password, user.password)

        if not correct_password:
            raise APIException('Incorrect Email or Password', status_code=status.HTTP_401_UNAUTHORIZED)

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response({'token': access_token})
        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)

        return response

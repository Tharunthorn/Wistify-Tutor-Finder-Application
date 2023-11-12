from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from .models import Learner
from .serializers import LearnerSerializer
from .serializers import LogInSerializer
from .serializers import SignUpSerializer
from .authentication import create_access_token
from .authentication import create_refresh_token
from django.contrib.auth.hashers import check_password


class GetLearner(APIView):
    def get(self, request):
        learner = Learner.objects.all()
        serializer = LearnerSerializer(learner, many=True)
        
        return Response(serializer.data)


class LearnerSignUp(APIView):
    def post(self, request):
        user_serializer = SignUpSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.validate(request.data)
        
        user = user_serializer.save()
        
        learner = Learner.objects.create(user=user)
        learner_seriailizer = LearnerSerializer(learner)
        
        return Response(learner_seriailizer.data)

    
class LearnerLogIn(APIView):
    def post(self, request): 
        login_serializer = LogInSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        login_serializer.validate(request.data)
                
        try:
            email = request.data['email']
            password = request.data['password']
            
            learner = Learner.objects.get(user__email=email)  
            
            correct_password = check_password(password, learner.user.password)
            
            if not correct_password:
                raise Learner.DoesNotExist
            
        except Learner.DoesNotExist:
            raise APIException('Incorrect Email or Password')
            
        access_token = create_access_token(learner.id)
        refresh_token = create_refresh_token(learner.id)
        
        response = Response()
        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }
        
        return response
    
    
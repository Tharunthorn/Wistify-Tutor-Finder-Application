from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
# from rest_framework.exceptions import APIException

from .models import Learner
from .serializers import UserSerializer, LearnerSerializer
from .models import User, Learner

@api_view(['GET'])
def getLearner(request):
    learner = Learner.objects.all()
    serializer = LearnerSerializer(learner, many=True)
    return Response(serializer.data)

class LearnerSignUp(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        learner = Learner.objects.create(user=user)
        learner_serializer = LearnerSerializer(data={"id": learner.id, "user": request.data})
        learner_serializer.is_valid(raise_exception=True)
        learner_serializer.save()
        return Response(learner_serializer.data)
    
# {
#  "email":"a.a@gmail.com",
# "first_name":"Bill",
# "last_name":"Gates",
# "password":"microsoft"
# }

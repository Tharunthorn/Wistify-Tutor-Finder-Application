from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from .models import Learner, Tutor, Rating, Tag, Video
from .serializers import LearnerSerializer, VideoSerializer
from .serializers import TutorSerializer, UserSerializer
from .serializers import LogInSerializer, SecondVideoSerializer
from .serializers import SignUpSerializer, SecondTagSerializer
from .serializers import RatingSerializer, SecondRatingSerializer
from .serializers import TagSerializer
from .authentication import create_access_token
from .authentication import create_refresh_token
from django.contrib.auth.hashers import check_password

class GetLearner(APIView):
    """Get all the learners' data in the application. """
    def get(self, request):
        learner = Learner.objects.all()
        serializer = LearnerSerializer(learner, many=True)
        
        return Response(serializer.data)

class GetTutor(APIView):
    """Get all the tutors' data in the application. """
    def get(self, request):
        tutor = Tutor.objects.all()
        serializer = TutorSerializer(tutor, many=True)
        
        return Response(serializer.data)
    
class GetRating(APIView):
    """Get all the ratings' data in the application. """
    def get(self, request):
        rating = Rating.objects.all()
        serializer = SecondRatingSerializer(rating, many=True)
        
        return Response(serializer.data)

class GetTag(APIView):
    """Get all the tags' data in the application. """
    def get(self, request):
        rating = Tag.objects.all()
        serializer = SecondTagSerializer(rating, many=True)
        
        return Response(serializer.data)
    
class GetVideo(APIView):
    """Get all the videos' data in the application. """
    def get(self, request):
        rating = Video.objects.all()
        serializer = SecondVideoSerializer(rating, many=True)
        
        return Response(serializer.data)
    
class LearnerSignUp(APIView):
    """Sign up and save learners' data. """
    def post(self, request):
        user_serializer = SignUpSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.validate(request.data)
        
        user = user_serializer.save()
        
        learner = Learner.objects.create(user=user)
        learner_seriailizer = LearnerSerializer(learner)
        
        return Response(learner_seriailizer.data)
    
class TutorSignUp(APIView):
    """Sign up and save tutors' data. """
    def post(self, request):
        user_serializer = SignUpSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.validate(request.data)
        
        user = user_serializer.save()
        
        tutor = Tutor.objects.create(user=user)
        tutor_seriailizer = TutorSerializer(tutor)
        
        return Response(tutor_seriailizer.data)

    
class LogIn(APIView):
    """
       Implementing the logging in for all the users 
       without role specification. 
    """
    def post(self, request): 
        login_serializer = LogInSerializer(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        login_serializer.validate(request.data)
        
        email = request.data['email']
        password = request.data['password']
        
        try:
            learner = Learner.objects.get(user__email=email)
            is_learner = True
            
        except Learner.DoesNotExist:
            
            try:
                # Check whether the user data belongs to the Tutor or not
                tutor = Tutor.objects.get(user__email=email)
                is_learner = False
                
            except Tutor.DoesNotExist:
                raise APIException('Incorrect Email or Password')

        user = learner.user if is_learner else tutor.user
        correct_password = check_password(password, user.password)

        if not correct_password:
            raise APIException('Incorrect Email or Password')
        
        # Generating Token session    
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)
        
        response = Response()
        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        user = UserSerializer(user)
        response.data = {
            'token': access_token,
            'user': user.data
        }
        
        return response
    

class UserRating(APIView):
    """Save and response the user's rating. """
    def post(self, request):
        rating_serializer = RatingSerializer(data=request.data)
        rating_serializer.is_valid(raise_exception=True)
        rating_serializer.validate(request.data)
        
        star = request.data['star']
        review = request.data['review']
        
        try:
            learner = Learner.objects.get(pk=request.data['learner_id'])
            tutor = Tutor.objects.get(pk=request.data['tutor_id'])
        except (Learner.DoesNotExist, Tutor.DoesNotExist):
            raise APIException("Learner or Tutor with the requested ID does not exist")
        
        try:
            rating = Rating.objects.get(learner=learner, tutor=tutor)
        except Rating.DoesNotExist:
            rating = Rating.objects.create(learner=learner, tutor=tutor, star=star, review=review)
        else:
           # This case means that the learner redo the same tutor rating again.
           # So, this will update the rating stars or rating review to the latest version.
           rating.star = star
           rating.review = review
           rating.save()
           
        second_rating = SecondRatingSerializer(rating)
        
        
        return Response(second_rating.data)
    
class AddVideo(APIView):
    """Save and response the uploaded video from tutor. """
    def post(self, request):
        video_serializer = VideoSerializer(data=request.data)
        video_serializer.is_valid(raise_exception=True)
        video_serializer.validate(request.data)
        
        tutor_id = request.data['tutor_id']
        url = request.data['url']
        
        try:
            tutor = Tutor.objects.get(pk=tutor_id)
        except Tutor.DoesNotExist:
            raise APIException('Tutor with the requested ID does not exist')  
        
        video = Video.objects.create(url=url, tutor=tutor)
        video = SecondVideoSerializer(video)
        
        return Response(video.data) 
    
class AddTag(APIView):
    """Save and response the tutor's tag. """
    def post(self, request):
        tag_serializer = TagSerializer(data=request.data)
        tag_serializer.is_valid(raise_exception=True)
        tag_serializer.validate(request.data)
        
        tutor_id = request.data['tutor_id']
        area = request.data['area']
        
        try:
            tutor = Tutor.objects.get(pk=tutor_id)
        except Tutor.DoesNotExist:
            raise APIException('Tutor with the requested ID does not exist')  
        
        tag = Tag.objects.create(area=area, tutor=tutor)
        tag = SecondTagSerializer(tag)
        
        return Response(tag.data) 
        
        
        
        
        
        
    
    
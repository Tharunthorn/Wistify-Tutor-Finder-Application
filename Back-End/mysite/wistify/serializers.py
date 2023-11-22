import string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Learner, Tutor, Rating, Video, Tag
from django.contrib.auth.hashers import make_password

# Get a set that contains all the uppercase and lowercase English
LETTERS = set(string.ascii_letters)


class UserSerializer(serializers.ModelSerializer):
    """Convert all the User fields into the JSON format. """
    
    class Meta:
        model = User
        fields = [
                  'email', 
                  'first_name', 
                  'last_name', 
                  'password', 
                  'profile_picture', 
                  'description']
        
class SignUpSerializer(serializers.ModelSerializer):
    """The collection of the sign Up essential data. """
    
    class Meta:
        model = User
        fields = [
                  'email', 
                  'first_name', 
                  'last_name', 
                  'password']
        
    def validate(self, data):
        right_format = set(data.keys()) == set(self.Meta.fields)
        
        data['first_name'] = data['first_name'].strip().title()
        data['last_name'] = data['last_name'].strip().title()
        
        # New created user needs to follow the naming rules.
        if not right_format:
            raise ValidationError("Wrong JSON data format")
        if not set(data['first_name']).issubset(LETTERS):
            raise ValidationError("First Name must be contained only English letters")
        if not len(data['first_name']) >= 2:
            raise ValidationError("First Name must be contained in the length of 2-20 English letters")
        if not set(data['last_name']).issubset(LETTERS):
            raise ValidationError("Last Name must be contained only English letters")
        if not len(data['last_name']) >= 2:
            raise ValidationError("Last Name must be contained in the length of 2-20 English letters")
        if not len(data['password']) >= 7:
            raise ValidationError("Password must be contained in the length of 7-20 characters")
        
        return data 
    
    def create(self, data):
        password = make_password(data['password'])
        data['password'] = password
        
        instance = self.Meta.model(**data)
        instance.save()
        return instance
        
         
class LearnerSerializer(serializers.ModelSerializer):
    """Convert all the learner fields into JSON format. """
    user = UserSerializer()
    
    class Meta:
        model = Learner
        fields = '__all__'
        
class TutorSerializer(serializers.ModelSerializer):
    """Convert all the tutor fields into the JSON format. """
    user = UserSerializer()
    
    class Meta:
        model = Tutor
        fields = '__all__'
  
        
class LogInSerializer(serializers.ModelSerializer):
    """Serializer with the email and Password fields as the major fields. """
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = [
                  "email",
                  "password"]
        
    def validate(self, data):
        right_format = set(data.keys()) == set(self.Meta.fields)
        
        if not right_format:
            raise ValidationError("Wrong JSON data format")

        return data 
    
class RatingSerializer(serializers.ModelSerializer):
    """Receiving the rating data. """
    # Identifying the learner and tutor can be specified from the primary key or id.
    learner_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)
    
    class Meta:
        model = Rating
        fields = ['star', 'review', 'learner_id', 'tutor_id']
        
    def validate(self, data):
        right_format = set(data.keys()) == set(self.Meta.fields)
        
        if not right_format:
            raise ValidationError("Wrong JSON data format")
        
        return data
    
class SecondRatingSerializer(serializers.ModelSerializer):
    """Responding the Rating data. """
    learner = LearnerSerializer()
    tutor = TutorSerializer()
    
    class Meta:
        model = Rating
        fields = '__all__'
        
class VideoSerializer(serializers.ModelSerializer):
    """Receiving the Video data. """
    tutor_id = serializers.IntegerField(required=True)
    
    class Meta:
        model = Video
        fields = ['url', 'tutor_id']
        
    def validate(self, data):
        right_format = set(data.keys()) == set(self.Meta.fields)
        
        if not right_format:
            raise ValidationError("Wrong JSON data format")
        
        return data
        
class SecondVideoSerializer(serializers.ModelSerializer):
    """Responding the Video data. """
    tutor = TutorSerializer()
    
    class Meta:
        model = Video
        fields = '__all__'
        
        
class TagSerializer(serializers.ModelSerializer):
    """Receiving the Tag data. """
    tutor_id = serializers.IntegerField(required=True)
    
    class Meta:
        model = Tag
        fields = ['area', 'tutor_id']
        
    def validate(self, data):
        right_format = set(data.keys()) == set(self.Meta.fields)
        
        if not right_format:
            raise ValidationError("Wrong JSON data format")
        
        return data
        
class SecondTagSerializer(serializers.ModelSerializer):
    """Responding the Video data. """
    tutor = TutorSerializer()
    
    class Meta:
        model = Tag
        fields = '__all__'
        
     
    
        
    
        

import string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Learner, Tutor, Rating
from django.contrib.auth.hashers import make_password

LETTERS = set(string.ascii_letters)
SCORE = {float(n) for n in range(1, 6)}


class UserSerializer(serializers.ModelSerializer):
    
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
    user = UserSerializer()
    
    class Meta:
        model = Learner
        fields = '__all__'
        
class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Tutor
        fields = '__all__'
  
        
class LogInSerializer(serializers.ModelSerializer):
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
    learner_id = serializers.IntegerField(required=True)
    tutor_id = serializers.IntegerField(required=True)
    
    class Meta:
        model = Rating
        fields = ['star', 'review', 'learner_id', 'tutor_id']
        
    def validate(self, data):
        right_format = set(data.keys()) == set(self.Meta.fields)
        
        if data['star'] not in SCORE:
            raise ValidationError("Wrong Score")
        
        if not right_format:
            raise ValidationError("Wrong JSON data format")
        
        return data
    
class RS(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'
        
     
    
        
    
        

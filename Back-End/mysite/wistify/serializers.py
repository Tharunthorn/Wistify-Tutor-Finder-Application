import string
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Learner
from django.contrib.auth.hashers import make_password

LETTERS = set(string.ascii_letters)


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
        if not right_format:
            raise ValidationError("Wrong JSON data format")

        return data 
    
    def create(self, data):
        password = make_password(data['password'])
        
        data['first_name'] = data['first_name'].title()
        data['last_name'] = data['last_name'].title()
        data['password'] = password
        
        instance = self.Meta.model(**data)
        instance.save()
        return instance
        
         
class LearnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Learner
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
        
     
    
        
    
        

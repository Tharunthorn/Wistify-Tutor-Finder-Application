from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Learner
from django.contrib.auth import authenticate


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
        
        if not right_format:
            raise ValidationError("Wrong JSON data format")

        return data  
        
        
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
        
     
    
        
    
        

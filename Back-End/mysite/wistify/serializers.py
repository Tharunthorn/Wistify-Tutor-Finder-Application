from rest_framework import serializers
from .models import User, Learner

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 
                  'first_name', 
                  'last_name', 
                  'password', 
                  'profile_picture', 
                  'description']
        
class LearnerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Learner
        fields = '__all__'
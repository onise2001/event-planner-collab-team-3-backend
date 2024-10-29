from rest_framework import serializers
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','password' ]
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self,validated_data):
        password = validated_data.pop('password')
        new_user = CustomUser(**validated_data)
        new_user.set_password(password)
        new_user.save()
        return new_user
from .models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required = True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    required=True,
    write_only=True,
    validators=[validate_password]
  )
  password2 = serializers.CharField(write_only=True, required=True)
  
  class Meta:
    model = User
    fields = ('username', 'password','password2', 'email')
  
  def validate(self, data):
    if data['password'] != data['password2']:
      raise serializers.ValidationError(
        {"password": "Passwrod fields didn't match"}
      )
    return data
  
  def create(self, validated_data):
    user = User.objects.create_user(
      email=validated_data['email'],
      username = validated_data['username'],
      password = validated_data['password'],
    )
    return user
  
  
class LoginSerializer(serializers.Serializer):
  password = serializers.CharField(write_only=True)
  username = serializers.CharField()
  
  def validate(self, data):
    user = authenticate( password = data['password'], username = data['username'])
    
    if user:
      token, _ = Token.objects.get_or_create(user=user)
      return {
        'token': token.key,
        'user_email': user.email,
        'nickname': user.username,
      }
    raise serializers.ValidationError("Invalid data")
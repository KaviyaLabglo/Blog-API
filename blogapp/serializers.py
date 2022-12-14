
from blogapp.models import Post, Comments

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework import serializers

from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from blogapp.models import User_Detail


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


# Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    token = serializers.SerializerMethodField('get_user_token')

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'token')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key


# Serializer to Get User Details using Django Token Authentication

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_user_token')

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name",
                  "username", "password", "token", "password"]

    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key


class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_Detail
        fields = ["user", "profile_picture", "phone",
                  "about_me",  "date_of_birth",  "gender"]


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
    
    
    
    
    
    
    
    
    
    
    
    

class PostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Post
        fields = ["post"]
        
       
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["comments", "post","url"]
        
        
class UserSerializer(serializers.ModelSerializer):
    Post = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    Comments = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    token = serializers.SerializerMethodField('get_user_token')


    class Meta:
        model = User
        fields = ["id", "first_name", "last_name",
                  "username", "password",  "Post", "Comments", "email", "token"]
        
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def get_user_token(self, obj):
        return Token.objects.get_or_create(user=obj)[0].key

        
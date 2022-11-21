
from blogapp.models import Post, Comments

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework import serializers

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

        
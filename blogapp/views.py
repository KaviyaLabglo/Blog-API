from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from blogapp.models import Post, Comments
from blogapp.serializers import PostSerializer, CommentsSerializer, UserSerializer
from blogapp.permissions import IsOwnerOrReadOnly

from rest_framework import permissions
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

class PostListView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
   

class CommentsListView(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                           ]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]
    
   
    
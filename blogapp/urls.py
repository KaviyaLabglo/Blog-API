
from blogapp.views import PostListView, CommentsListView, UserView
from django.urls import path, include



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostListView)
router.register(r'comments', CommentsListView)
router.register(r'user', UserView)


urlpatterns = [
   
   path('', include(router.urls)),

   
]



from blogapp.views import (PostListView, 
      CommentsListView, 
      UserViewSet, 
      User_Detail_ViewSet,
      RegisterUserAPIView, 
      LoginView,
      LogoutView,
      UserDetailAPI,
      ChangePasswordView
      )
from django.urls import path, include



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post', PostListView)
router.register(r'comments', CommentsListView)


router.register(r'users', UserViewSet)
router.register(r'user-information', User_Detail_ViewSet)
urlpatterns = [
   
   path('', include(router.urls)),
   
   path('register', RegisterUserAPIView.as_view(), name="register"),
   path('log/', LoginView.as_view()),
   path('logout/', LogoutView.as_view()),

    # Login User Detail
   path('loginuser-detail/', UserDetailAPI.as_view()),
    # Change the user password
   path('change_password/<int:pk>/', ChangePasswordView.as_view(),
         name='auth_change_password'),

   
]


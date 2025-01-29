from django.urls import path
from .views.listall import UserProfileListAPIView
from .views.singlecreate import UserProfileCreateAPIView
from .views.singledetails import UserProfileRetrieveAPIView
from .views.singleupdate import UserProfileUpdateAPIView
from .views.singledelete import UserProfileDeleteAPIView

from .views.register import RegisterView
from .views.login import LoginView, RefreshTokenView
from .views.verify2FA import VerifySecurityCode
from .views.forget_password import SecurityCode, ResetPassword


urlpatterns = [
    path('profiles', UserProfileListAPIView.as_view(), name='user-profile-list'),
    path('profiles/create', UserProfileCreateAPIView.as_view(), name='user-profile-create'),
    path('profiles/<int:pk>', UserProfileRetrieveAPIView.as_view(), name='user-profile-retrieve'),
    path('profiles/<int:pk>/update', UserProfileUpdateAPIView.as_view(), name='user-profile-update'),
    path('profiles/<int:pk>/delete', UserProfileDeleteAPIView.as_view(), name='user-profile-delete'),

    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('verify', VerifySecurityCode.as_view(), name='2faVerify'),
    path('sendemail', SecurityCode.as_view(), name='sendemail'),
    path('resetpassword', ResetPassword.as_view(), name='resetpassword'),

    path('refreshtoken', RefreshTokenView.as_view(), name='refreshtoken'),


    
]

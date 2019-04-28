from django.urls import path, include
from . import views
from rest_auth.urls import PasswordResetConfirmView

urlpatterns = [path('rest-auth/', include('rest_auth.urls')),
               path('rest-auth/', include('django.contrib.auth.urls')),
               path('register/', views.UserCreate.as_view(), name='register'),
               ]

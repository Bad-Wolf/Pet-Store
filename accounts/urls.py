from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

#app_name = "accounts"

urlpatterns = [path('', include('django.contrib.auth.urls')),
               path('profile/', views.redirect_to_user_details, name='redirect-user-details'),
               path('profile/<pk>/', views.UserDetails.as_view(), name='user-details'),
               path('signup/', views.SignUp.as_view(), name='signup'),
               path('password-change/',
                    auth_views.PasswordChangeView.as_view(template_name='change-pass.html'),
                    name='password_change'),
               path('password-change/done/',
                    auth_views.PasswordChangeDoneView.as_view(template_name='change-pass-done.html'),
                    name='password_change_done'),
               ]

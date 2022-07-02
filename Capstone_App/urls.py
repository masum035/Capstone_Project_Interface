from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('home/', views.signUp, name='sign_up'),
    # path('upload/', views.chunkWiseFileUpload, name='file-chunk'),
    path('signin/', views.loggin, name='sign_in'),

    path('<slug:anything>', views.error, name='error'),
    path('accounts/social/signup/',views.error, name='login-Error'),
    path('accounts/logout/', LogoutView.as_view(), name='auth_logout'),

]

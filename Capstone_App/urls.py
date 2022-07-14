from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('home/', views.index_section, name='home'),
    path('upload/', views.start_working, name='file_upload'),
    # path('upload/', views.chunkWiseFileUpload, name='file-chunk'),
    path('signup/', views.signUp, name='sign_up'),
    path('signin/', views.loggin, name='sign_in'),
    path('aboutUs/', views.about_us, name='about_us'),
    path('FAQ/', views.faq_section, name='faq'),
    path('workplan/', views.workplan_section, name='work_plan'),
    path('result/', views.result_section, name='result'),

    path('<slug:anything>', views.error, name='error'),
    path('accounts/social/signup/', views.error, name='login-Error'),
    path('accounts/logout/', LogoutView.as_view(), name='auth_logout'),

]

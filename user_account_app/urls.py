from allauth.socialaccount.providers.github import views as github_views
from django.urls import path
from .views import GithubLogin, github_callback
urlpatterns = [
    path('', GithubLogin.as_view(), name= 'github_login'),
    # path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('google/login/', GoogleLogin.as_view(), name='google_login'),

    path('auth/github/callback/', github_callback, name='github_callback'),
    path('auth/github/url/', github_views.oauth2_login)

    
]
    
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
    
    
    ### secret - 046555f075a58755a543ff4649f55405c434b5aa
    ## key=  e58cb4553d1d3ad7b0d0
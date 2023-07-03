from django.shortcuts import render, redirect
import urllib.parse
from django.urls import reverse

from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework.response import Response
import urllib.parse


class GithubLogin(SocialLoginView):
    adapter_class= GitHubOAuth2Adapter
    client_class= OAuth2Client
    
    @property
    def callback_url(self, request):
        return self.request.build_absolute_uri(reverse('github_callback'))
    
    
def github_callback(request):
    params = urllib.parse.urlencode(request.GET)
    return redirect(f'https://frontend/user-account/auth/github?{params}')



  
          
# class FacebookLogin(SocialLoginView):
#     adapter_class= FacebookOAuth2Adapter
    

# class GoogleLogin(SocialLoginView):
#     adapter_class= GoogleOAuth2Adapter

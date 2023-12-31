
from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path("user-account/", include('user_account_app.urls')),
    
    ### 
    path("", TemplateView.as_view(template_name= 'index.html'), name="home"),
    path("accounts/", include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    
]
 

#

   
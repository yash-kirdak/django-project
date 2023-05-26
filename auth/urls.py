from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup, name="signup"),
    path('login',views.Login, name="login"),
    path('logout',views.Logout, name="logout"),
    #path('show',views.show,name="show")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



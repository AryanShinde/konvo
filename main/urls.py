from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    path('', views.homepage, name="home"),
    path('logout/', views.logout_view, name='logout')
]
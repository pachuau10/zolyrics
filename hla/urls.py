from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('hla/<str:name>/', views.hla, name='hla'),
    path('request/', views.request_view, name='request')
]

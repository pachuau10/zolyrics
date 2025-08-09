from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('hla/',views.hla,name="hla"),
    path('hla/<int:pk>/',views.hla,name="hla")

]
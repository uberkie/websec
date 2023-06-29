from django.urls import path
from netsec import views

appname = 'netsec'
urlpatterns = [

    path('', views.registration, name='registration'),

]

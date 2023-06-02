from django.urls import path
from uk.views import *

app_name='uk'

urlpatterns=[
    path('australia/',australia,name='australia'),
    path('swan/',swan,name='swan')
]
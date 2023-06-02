from django.urls import path
from usa.views import *

app_name='usa'

urlpatterns=[
    path('europe/',europe,name='europe'),
    path('peacock/',peacock,name='peacock'),
]
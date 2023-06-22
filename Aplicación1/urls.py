from django.urls import path
from Aplicación1 import views

urlpatterns=[
    path('',views.HolaMundo,name='HolaMundo'),
]
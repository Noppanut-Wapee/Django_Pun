from django.urls import path, include
from .views import HomePage
urlpatterns = [  
    # localhost:8000/
    path('',HomePage),
]

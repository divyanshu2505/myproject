
from django.urls import path
from .import views
#localhost: 8000/chai
#localhost: 8000/chai/all_chai
urlpatterns = [
    
    path('', views.home, name='home')
]
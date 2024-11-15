from django.urls import path
from .views import (
    home,
    about,
    courses,
    partner, 
    alumnis,
    contact,
    enroll,
    partner,
    alumnis,
    


    
)

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'), 
    path('courses/', courses, name='courses'), 
    path('partner/', partner, name='partner'), 
    path('alumnis/', alumnis, name='alumnis'), 
    path('contact/', contact, name='contact'), 
    path('enroll/', enroll, name='enroll'), 
    path('partner/', partner, name='partner'),
    path('alumnis/', alumnis, name='alumnis'),
    
    
    
]

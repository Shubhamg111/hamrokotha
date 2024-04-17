
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('contactpage',views.contactpage,name="contacts"),
    path('aboutpage',views.aboutpage,name="aboutpage"),
    path('servicespage',views.servicespage,name="servicespage"),
]
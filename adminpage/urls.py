from django.urls import path
from accounts import views
from . import views

urlpatterns = [
    path('adminpage',views.adminpage,name="adminpage"),
    path('postview',views.postview,name="postview"),
    path('aboutpage',views.aboutpage,name="aboutpage"),
    path('servicespage',views.servicespage,name="servicespage"),
    path('contactpage',views.contactpage,name="contactpage"),

    

    

]

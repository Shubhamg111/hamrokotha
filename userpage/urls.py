from django.urls import path
from accounts import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('userpage',views.userpage,name="userpage"),
    # path('category',views.category,name="category")
    path('uploadpost',views.uploadpost,name="uploadpost"),
    path('postlist',views.postlist,name="postlist"),
    path('aboutpage',views.aboutpage,name="aboutpage"),
    path('servicespage',views.servicespage,name="servicespage"),
    path('contactpage',views.contactpage,name="contactpage"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('accounts.urls')),
    path('admins/',include('adminpage.urls')),
    path('user/',include('userpage.urls')),
    path('',include('pages.urls')),



]

# add at the last
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


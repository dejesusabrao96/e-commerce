from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings
from django.conf import settings
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
    path('' , include('adminapp.urls')),
    path('report/' , include('report.urls')),
    path('custom/', include('custom.urls')),
    path('utilizador/', include('users.urls')),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/notification/', include('notification.api.urls')),
    path('notification/', include('notification.urls')),
    path('api/', include('api.urls')),

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
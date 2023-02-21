from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('stdlogin', views.stdlogin, name='stdlogin'),
    path('revlogin', views.revlogin, name='revlogin'),
    path('rev', views.admin1, name='rev'),
    path('adminrev', views.adminrev, name='adminrev'),
    path('student', views.student, name='student'),
    path('submitrev', views.submitReviwe, name='submitReviwe'),
    path('stdupdateprofile', views.stdupdate, name='stdupdate'),
    path('stdupdatedone', views.stdupdatedone, name='stdupdatedone'),
] 
if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL,
                              document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
<<<<<<< HEAD:aero_facil/urls.py
    path("admin/", admin.site.urls),
    path("", include("core.urls")),   # inclui as urls do app core
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
=======
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # rota principal
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> ebe07c42394dbd8e6ae65bef6ac3c7c68e7a8509:config/urls.py

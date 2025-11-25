<<<<<<< HEAD
"""
URL configuration for aero_facil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
=======
>>>>>>> 17871da0eda8ce5e054c70958a1c87ed3c534fa2
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

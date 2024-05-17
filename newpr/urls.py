"""
URL configuration for newpr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Online News"
admin.site.site_title = "Yangiliklar dunyosi "
admin.site.index_title = "Hush kelibsiz !..."

urlpatterns = ([
                   path('admin/', admin.site.urls),
                   path('news/', include('newapp.urls', namespace='news')),
                   path('', include('users.urls', namespace='users')),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                            document_root=settings.
                                                                                            MEDIA_ROOT))

"""
URL configuration for products project.

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
from django.urls import path

# from courses.views import index
# from courses.views import *
from django.contrib import admin
from django.urls import path, include

from courses.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("courses/", index), # маршрут нашей страницы http://127.0.0.1:8000/courses/
    # path("", index), # маршрут нашей страницы http://127.0.0.1:8000
    # path("courses", include('courses.urls')), # ссылка на файл приложения, где хранятся адреса
    path("", include('courses.urls')),
    # path('^api/', include('courses.api.urls', namespace='api')),
]

handler404 = pageNotFound
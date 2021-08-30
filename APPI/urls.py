"""APPI path Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .router import router
from myapp import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from django.urls.conf import include

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
      description="Employee description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@abc.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('', views.API.as_view()),
    path('', views.home, name='home'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


##please use  "python manage.py runserver 8080" this to run server as port 8000 is used by  PostgreSQL .
## use "/" in the end of every url or after perticular id number in url, or it will throw an error of page not found
## same applicable in POSTMAN also.
## admin page ID = admin, password = admin
## for search field "127.0.0.1:8080/api/employee/?search=23" use this format in url (replace 23 with search item)
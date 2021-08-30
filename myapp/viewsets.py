from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.generics import GenericAPIView
# from .models import employee
# from .serializers import employeeserializer
from . import models
from . import serializers
from rest_framework.filters import SearchFilter


class API(GenericAPIView):
    serializer_class = serializers.employeeserializer

class employeeviewsets(viewsets.ModelViewSet):
    queryset = models.employee.objects.all()
    serializer_class = serializers.employeeserializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'id', 'age', 'department']

class deptviewsets(viewsets.ModelViewSet):
    queryset = models.department.objects.all()
    serializer_class = serializers.deptserializer
    filter_backends = [SearchFilter]
    search_fields = ['dept_name', 'id']

##please use  "python manage.py runserver 8080" this to run server as port 8000 is used by  PostgreSQL .
## use "/" in the end of every url or after perticular id number in url, or it will throw an error of page not found
## same applicable in POSTMAN also.
## for search field "127.0.0.1:8080/api/employee/?search=23" use this format in url (replace 23 with search item)
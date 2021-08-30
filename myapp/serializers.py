from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import employee, department

class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id', 'name', 'age', 'department']

class deptserializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = ['id', 'dept_name']

##please use  "python manage.py runserver 8080" this to run server as port 8000 is used by  PostgreSQL .
## use "/" in the end of every url or after perticular id number in url, or it will throw an error of page not found
## same applicable in POSTMAN also.
## admin page ID = admin, password = admin
## for search field "127.0.0.1:8080/api/employee/?search=23" use this format in url (replace 23 with search item)
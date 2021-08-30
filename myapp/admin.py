from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import employee, department

# Register your models here.
admin.register(employee)
class adminpage(admin.ModelAdmin):
    list_display = ['name', 'age', 'department']

admin.register(department())
class adminpage(admin.ModelAdmin):
    list_display = ['dept_name']

##please use  "python manage.py runserver 8080" this to run server as port 8000 is used by  PostgreSQL .
## use "/" in the end of every url or after perticular id number in url, or it will throw an error of page not found
## same applicable in POSTMAN also.
## admin page ID = admin, password = admin
## for search field "127.0.0.1:8080/api/employee/?search=23" use this format in url (replace 23 with search item)

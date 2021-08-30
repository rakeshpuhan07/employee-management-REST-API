from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=100)

class department(models.Model):
    dept_name = models.CharField(max_length=50)


##please use  "python manage.py runserver 8080" this to run server as port 8000 is used by  PostgreSQL .
## use "/" in the end of every url or after perticular id number in url, or it will throw an error of page not found
## same applicable in POSTMAN also.
## admin page ID = admin, password = admin
## for search field "127.0.0.1:8080/api/employee/?search=23" use this format in url (replace 23 with search item)
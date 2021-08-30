from django.shortcuts import render
from .models import employee, department
from rest_framework.generics import GenericAPIView
from .serializers import employeeserializer

# Create your views here.
# class API(GenericAPIView):
#     serializer_class = employeeserializer()
def home(request):
    return render(request, 'home.html')

##please use  "python manage.py runserver 8080" this to run server as port 8000 is used by  PostgreSQL .
## use "/" in the end of every url or after perticular id number in url, or it will throw an error of page not found
## same applicable in POSTMAN also.
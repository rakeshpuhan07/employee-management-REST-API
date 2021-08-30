from myapp.viewsets import employeeviewsets, deptviewsets, API
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', employeeviewsets, API)
router.register('department', deptviewsets)
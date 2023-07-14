from django.urls import path
from .views import *

app_name = 'academy'

urlpatterns = [
    path('application/', ApplicationCreate.as_view()),
    path('departments/', DepartmentList.as_view()),
]

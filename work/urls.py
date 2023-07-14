from django.urls import path
from .views import WorkCreate

app_name = 'work'

urlpatterns = [
    path('work/', WorkCreate.as_view()),
]

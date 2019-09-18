from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('data/', views.SampleData.as_view()),
]

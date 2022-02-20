from django.urls import path
from  . import views

app_name = 'main'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('api/<str:name_request>', views.api_test, name='api'),
    path('add_memory/', views.add_memory, name='add_memory'),
    path('check_memory/', views.check_memory, name='check_memory'),
    path('memory_form/', views.get_memory, name='memory_form'),
]
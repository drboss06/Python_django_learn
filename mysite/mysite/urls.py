from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('main.urls')),
    path('add_place/', include('main.urls')),
    path('add_memory/', include('main.urls')),
    path('check_memory/', include('main.urls'))
]

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', include('polls.urls'))
]'''

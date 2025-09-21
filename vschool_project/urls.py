from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vschool.urls')),   # link your app
    path('api/assignments/', include('assignments.urls')),
    path('api/', include('vschool.urls')),
]


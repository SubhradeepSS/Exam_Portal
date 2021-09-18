from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('prof/', include('prof.urls')),
    path('student/', include('student.urls')),
]

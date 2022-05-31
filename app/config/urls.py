from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('api.urls')), # change it
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

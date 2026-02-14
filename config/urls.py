from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/petrol-spy/', include('petrol_spy.urls')),
]

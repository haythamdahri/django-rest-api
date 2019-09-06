from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('todos.urls'))
]

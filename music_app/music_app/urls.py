from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # Whenever urls are not admin or api, redirected to the frontend
    path('', include('frontend.urls'))
]

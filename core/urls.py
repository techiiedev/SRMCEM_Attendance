from django.contrib import admin
from django.urls import path, include
from attendance.views import logout_view # Import your custom logout

urlpatterns = [
    # Route admin logout to YOUR custom logout view before admin.site.urls
    path('admin/logout/', logout_view), 
    path('admin/', admin.site.urls),
    path('', include('attendance.urls')),
]
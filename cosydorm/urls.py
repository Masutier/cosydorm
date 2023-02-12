from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *

# admin.site.site_header = "Cosy Dorm Cleaning Admin"
# admin.site.site_title = "Cosy Dorm Cleaning Admin"
# admin.site.index_title = "Welcome To Cosy Dorm Cleaning Admin"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('laundry', laundry, name='laundry'),
    path('cleaning', cleaning, name='cleaning'),
    path('storage', storage, name='storage'),

    # path('privacy', privacy, name='privacy'),
    # path('page401', page401, name='page401'),

    # path('', include('pdf_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 401 Unauthorized
# 403 Forbidden
# 404 Not Found

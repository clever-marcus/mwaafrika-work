from django.contrib import admin
from django.urls import path, include
from user.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls', namespace='user'))
]

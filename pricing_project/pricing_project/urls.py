

from django.contrib import admin
from django.urls import path, include
from pricing.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pricing/', include('pricing.urls')),
    path('',welcome),

]

from django.contrib import admin
from django.urls import path, include

import blog, user, animals, main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('animals/', include('animals.urls')),
    path('user/', include('user.urls')),
]

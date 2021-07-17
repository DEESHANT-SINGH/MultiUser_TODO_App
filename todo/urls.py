
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))      # app folder --> urls.py => app.urls  (path)
]

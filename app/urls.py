# To handle all urls (map or link all urls) -> like localhost:8000/home, localhost:8000/login, localhost:8000/orders ,etc

from django.contrib import admin
from django.urls import path
from app.views import home, login, signup, add_todo, signout, delete_todo, change_todo     # from views.py importing functions


urlpatterns = [
    path('',home, name='home'),
    path('login/',login, name='login'),  
    path('signup/',signup), 
    path('add-todo/',add_todo),
    path('delete-todo/<int:id>' , delete_todo),      # <int:id> takes dynamic values like --> delete-todo/1/
    path('change-status/<int:id>/<str:status>' , change_todo), 
    path('logout/',signout),
]

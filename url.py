
from django.contrib import admin
from django.urls import path, include
from todo_list import views

urlpatterns = [
    #path to the admin site for todo_list
    path('admin/', admin.site.urls),
    #path to the home page for todo_list
    path('', include('todo_list.urls')),
]

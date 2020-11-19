from django.urls import path
from . import views

urlpatterns = [
	#path to the home page
	path('', views.home, name="home"),
	#path to the delete function
	path('delete/<list_id>', views.delete, name="delete"),

    #path to cross off function
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    #path to uncross function
    path('uncross/<list_id>', views.uncross, name="uncross"),
    #path to the edit page
    path('edit/<list_id>', views.edit, name="edit"),
]

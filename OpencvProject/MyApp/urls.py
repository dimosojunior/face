#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('face_detection/', views.face_detection, name="face_detection"),
    path('', views.home, name="home"),
    path('welcome/', views.welcome, name="welcome"),
    path('base/', views.base, name="base"),
    path('detect/', views.detect, name="detect"),
    path('criminals_records/', views.criminals_records, name="criminals_records"),
    path('view_criminals_records/<int:id>/', views.view_criminals_records, name="view_criminals_records"),
    #path('search_criminal/', views.search_criminal, name="search_criminal"),
    path('search_criminal_autocomplete', views.search_criminal_autocomplete, name="search_criminal_autocomplete"),
    path('add_criminal/', views.add_criminal, name="add_criminal"),
    
    path('all_criminals/', views.all_criminals, name="all_criminals"),
    path('update_criminal/<int:id>/', views.update_criminal, name="update_criminal"),
    path('delete_criminal/<int:id>/', views.delete_criminal, name="delete_criminal"),


    path('add_criminal_records/', views.add_criminal_records, name="add_criminal_records"),
    path('update_criminal_records/<int:id>/', views.update_criminal_records, name="update_criminal_records"),
    path('delete_criminal_records/<int:id>/', views.delete_criminal_records, name="delete_criminal_records"),
    
    
]

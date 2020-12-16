from django.urls import path

from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('logins',views.logins,name='logins'),
    path('submit',views.submit,name='submit'),  
    path('newlogin',views.newlogin,name='newlogin'),  

]
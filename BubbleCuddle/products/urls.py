from django.urls import path
from products import views
urlpatterns = [
    path('', views.home),
    path('ourstory/', views.ourstory),
     path('contactus/', views.contactus),

]
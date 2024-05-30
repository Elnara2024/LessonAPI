from django.db import router
from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()

routers.register("car-marks", views.CarMarkViewSet)
routers.register('cars', views.CarViewset)


urlpatterns = [
    #path('car-marks/', views.CarMarkListCreateView.as_view()),
    #path('car-marks/<int:pk>/', views.CarMarkUpdateDeleteView2.as_view()),
    #path('cars/', views.CarListView2.as_view()),
    #path('car-create/', views.CarCreateView2.as_view()),
    #path('car-detail/<int:pk>/', views.CarDetailView2.as_view()),
    #path('car-delete/<int:pk>/', views.CarDestroyView2.as_view()),
    #path('car-update/<int:pk>/', views.CarUpdateView2.as_view()),

    path('', include(routers.urls))
]

"""
/api/car-marks/GET -> listing
/Opi/car-marks/POST -> create
/api/car-marks/<int: pk>/ PUT -> Update 
/api/car-marks/<int: pk>/ Delete -> Delete



/api/cars/ GET 
/api/cars/ POST
/api/cars/<int:pk>/ CET
/api/cars/<int: pk>/ PUT 
/api/cars/<int:pk>/ DELETE

"""

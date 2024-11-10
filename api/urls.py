from django.urls import path
from .views import *
urlpatterns = [
    path('create-employee/', CreateEmployeeApi.as_view(), name='create-employee'),
    path('retrieve-employee/<int:pk>/', RetrieveEmployeeApi.as_view(), name='retrieve-employee'),
    path('update-employee/<int:pk>', UpdateEmployeeApi.as_view(),name='update-employee'),
    path('search-employee/<str:employee_name>/', SearchEmployeeApi.as_view(), name='search-employee'),
    path('delete-recipe/<int:pk>/', DeleteEmployeeApi.as_view(),name='delete-employee'),
]
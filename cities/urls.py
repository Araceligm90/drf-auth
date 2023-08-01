from django.urls import path
from .views import CityList, CityDetail

urlpatterns = [
    path('', CityList.as_view(), name='city_list'),
    path('<int:pk>/', CityDetail.as_view(), name="city_detail"),
]

from django.urls import path

from device_location_app import views


urlpatterns = [
    path('latest-info/<int:device_id>/', views.DeviceLatestInfo.as_view(), name='LatestInfo'),
    path('journey/<int:device_id>/', views.StartEndLocation.as_view(), name='LatestInfo'),
    path('locations/<int:device_id>/<str:start_time_str>/<str:end_time_str>/', views.AllLocationCoordinates.as_view( ), name='GetLocationPoints'),
]
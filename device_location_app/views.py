from device_location_app.models import DeviceLocation
from device_location_app.serializers import DeviceLocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from django.conf import settings
from rest_framework import status
from django.utils.dateparse import parse_datetime


CACHE_TTL = getattr(settings, 'CACHE_TTL', 30)


class DeviceLatestInfo(APIView):
    def get(self, request, device_id):
        cache_key = 'DeviceLatestInfo'+str(device_id)
        if cache.get(cache_key):
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)
        else:
            device = DeviceLocation.objects.filter(device_fk_id=device_id).order_by('-sts').first()

        if device:
            serializer = DeviceLocationSerializer(device)
            print('cache_hit')
            cache.set(cache_key, serializer.data, CACHE_TTL)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"message": "Device ID not found"}, status=status.HTTP_404_NOT_FOUND)


class StartEndLocation(APIView):
    def get(self, request, device_id):
        cache_key = 'StartEndLocation' + str(device_id)
        if cache.get(cache_key):
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)           
        start_location = DeviceLocation.objects.filter(device_fk_id=device_id).order_by('time_stamp').first()
        end_location = DeviceLocation.objects.filter(device_fk_id=device_id).order_by('-time_stamp').first()

        if start_location and end_location:
            start_lat_lon = (start_location.latitude, start_location.longitude)
            end_lat_lon = (end_location.latitude, end_location.longitude)
            response_data = {
                'start_location': start_lat_lon,
                'end_location': end_lat_lon
            }
            cache.set(cache_key, response_data, CACHE_TTL)
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'message': 'Device ID not found'}, status=status.HTTP_404_NOT_FOUND)


class AllLocationCoordinates(APIView):
    def get(self, request, device_id, start_time_str, end_time_str):
        try:
            start_time = parse_datetime(start_time_str)
            end_time = parse_datetime(end_time_str)
            if start_time>end_time:
                raise ValueError
        except ValueError:
            return Response({'message': 'Invalid time format or values. Please provide time in ISO 8601 format (e.g., "2022-04-01T00:00:00Z")'}, status=status.HTTP_400_BAD_REQUEST)

        cache_key = 'AllLocationCoordinates' + str(device_id) + start_time_str + end_time_str
        if cache.get(cache_key):
            return Response(cache.get(cache_key), status=status.HTTP_200_OK)
        
        location_points = DeviceLocation.objects.filter(device_fk_id=device_id, time_stamp__range=(start_time, end_time)).order_by('time_stamp')
        if not location_points:
            Response({'message': 'Device ID not found'}, status=status.HTTP_404_NOT_FOUND)

        serialized_location_points = []
        for point in location_points:
            serialized_location_points.append({
                'latitude': point.latitude,
                'longitude': point.longitude,
                'time_stamp': point.time_stamp.strftime('%Y-%m-%d %H:%M:%S')  # Convert to string format if needed
            })
        
        cache.set(cache_key, serialized_location_points, CACHE_TTL)
        return Response(serialized_location_points, status=status.HTTP_200_OK)
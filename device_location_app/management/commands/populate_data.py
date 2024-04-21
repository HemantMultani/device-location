from django.core.management.base import BaseCommand
from device_location_app.models import DeviceLocation
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        import pandas as pd
        
        directory = "media/raw_data"
        filename = "raw_data (4) (6).csv"
        file_path = os.path.join(directory, filename)
        
        data = pd.read_csv(file_path)
        data['time_stamp'] = pd.to_datetime(data['time_stamp'])
        data['sts'] = pd.to_datetime(data['sts'])
        data = data.sort_values(by='sts')
        
        for index, row in data.iterrows():
            DeviceLocation.objects.create(
            device_fk_id=row['device_fk_id'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            time_stamp=row['time_stamp'],
            sts=row['sts'],
            speed=row['speed']
    )

from django.db import models

# Create your models here.
class DeviceLocation(models.Model):
    device_fk_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    time_stamp = models.DateTimeField()
    sts = models.DateTimeField()
    speed = models.IntegerField()  # Assuming speed is an integer field

    def __str__(self):
        return f"Location data for Device {self.device_fk_id}"
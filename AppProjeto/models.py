from django.contrib.gis.db import models


class UserModels(models.Model):
    id_Gps = models.AutoField(primary_key=True)
    latitude = models.PointField()
    longitude = models.PointField()

    def __str__(self):
        return f'id_Gps: {self.id_Gps} | latitude: {self.latitude} | longitude: {self.longitude}'

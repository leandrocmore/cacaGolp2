from django.db import models


class UserModels(models.Model):
    id_Gps = models.AutoField(primary_key=True)
    latitude = models.CharField(max_length=13, default= 0)
    longitude = models.CharField(max_length=13, default= 0)

    def __str__(self):
        return f'id_Gps: {self.id_Gps} | latitude: {self.latitude} | longitude: {self.longitude}'

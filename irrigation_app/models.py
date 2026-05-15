from django.db import models


# 🌍 FARM MODEL
class Farm(models.Model):
    farmer_id = models.IntegerField()
    boundary = models.JSONField()   # polygon coords
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Farm {self.id} - Farmer {self.farmer_id}"


# 📍 ZONE MODEL
class Zone(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="zones")
    zone_number = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Zone {self.zone_number} (Farm {self.farm.id})"


# 📊 SENSOR DATA (UPDATED)
class SensorData(models.Model):
    zone = models.ForeignKey(
    Zone,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    moisture = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField(default=0)

    irrigation_decision = models.CharField(max_length=10, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zone {self.zone.zone_number} - Moisture: {self.moisture}"
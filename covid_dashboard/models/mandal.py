from django.db import models
from covid_dashboard.models.district import District

class Mandal(models.Model):
    name = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

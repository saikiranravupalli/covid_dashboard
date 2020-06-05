from django.db import models
from covid_dashboard.models.mandal import \
    Mandal

class DailyStatistics(models.Model):
    for_date = models.DateField()
    total_confirmed = models.IntegerField()
    total_deaths = models.IntegerField()
    total_recovered = models.IntegerField()
    mandal = models.ForeignKey(Mandal, on_delete=models.CASCADE)

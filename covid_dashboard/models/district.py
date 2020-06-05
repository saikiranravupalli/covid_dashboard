from django.db import models
from covid_dashboard.models.state import \
    State

class District(models.Model):
    name = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)

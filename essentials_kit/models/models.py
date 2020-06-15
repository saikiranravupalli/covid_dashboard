from django.db import models
from django.contrib.auth.models import AbstractUser
import enum
from ib_common.constants import BaseEnumClass

class StatusEnum(BaseEnumClass, enum.Enum):
    Live = "Live"
    Done = "Done"
    Closed = "Closed"
    Draft = "Draft"

FORM_CHOICES = StatusEnum.get_list_of_tuples()

class User(AbstractUser):
    name = models.CharField(max_length=100)
    profile_pic = models.URLField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    role = models.CharField(default="user")

class Form(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    name = models.CharField(max_length=100)
    instructions = models.TextField()
    closes_on = models.DateTimeField()
    form_status = models.CharField(
        max_length=30,
        choices=FORM_CHOICES,
        default=StatusEnum.Draft.value
    )
    expected_delivery_date = models.DateTimeField()

class Section(models.Model):
    name = models.CharField(max_length=20)
    note = models.TextField()
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name="forms"
    )

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="sections"
    )

class Brand(models.Model):
    name = models.CharField(max_length=100)
    item = models.ManyToManyField(Item, through="ItemsQuantity")

class ItemsQuantity(models.Model):
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

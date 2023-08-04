from django.db import models
import uuid

class PhoneUsers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    date_create = models.DateField(auto_now_add=True, editable=False)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


from django.db import models
import uuid


class PhoneUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_auto_generated = models.BooleanField(blank=False, default=False)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date_create = models.DateField(auto_now_add=True, editable=False)
    date_update = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return (
            f"Имя {self.name} "
            f"|| номер {self.phone_number} "
            f"|| дата создания {self.date_create} "
            f"|| дата изменения {self.date_update}"
        )

    __repr__ = __str__

    class Meta:
        ordering = ["name"]
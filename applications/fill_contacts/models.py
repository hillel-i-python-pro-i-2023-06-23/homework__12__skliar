from django.db import models
import uuid


class PhoneUser(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )  # не понял в чем проблема
    is_auto_generated = models.BooleanField(default=False)  # исправил
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date_create = models.DateField(auto_now_add=True, editable=False)
    date_update = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return (
            f"ID {self.id} "
            f"|| Имя {self.name} "
            f"|| номер {self.phone_number} "
            f"|| дата создания {self.date_create} "
            f"|| дата изменения {self.date_update}"
        )

    __repr__ = __str__

    class Meta:  # для сортировки
        ordering = ["name"]

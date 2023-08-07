from applications.fill_contacts.models import PhoneUser
import uuid
from datetime import date


def add_phone_user(name, phone_number, is_auto_generated=False):
    new_user = PhoneUser.objects.create(
        id=uuid.uuid4(),
        is_auto_generated=is_auto_generated,
        name=name,
        phone_number=phone_number,
        date_create=date.today(),
        date_update=date.today(),
    )
    return new_user

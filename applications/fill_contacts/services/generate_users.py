from typing import Iterator
from faker import Faker

from applications.fill_contacts.models import PhoneUser


def generate_user():
    return PhoneUser(
        name=Faker().first_name(),
        phone_number=Faker().phone_number(),
    )


def generate_users(amount: int) -> Iterator[PhoneUser]:
    for _ in range(amount):
        yield generate_user()

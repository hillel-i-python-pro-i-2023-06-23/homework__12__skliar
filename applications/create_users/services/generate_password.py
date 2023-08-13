import string
import random
import logging
from applications.create_users.services.init_user import UserData


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generate_password():
    characters = string.ascii_letters + string.digits + r"#$%!_*&"
    while True:
        length = random.randint(8, 20)
        password = "".join(random.choice(characters) for _ in range(length))
        try:
            UserData._validate_password(password)
            logger.info(f"Generated valid password: {password}")
            return password
        except ValueError as ex:
            logger.warning(f"Generated invalid password: {password}. Reason: {ex}")
            # Если пароль не проходит валидацию, генерируем новый пароль
            continue
    return password

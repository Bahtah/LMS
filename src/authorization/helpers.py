import random
import string
import secrets


def generate_code():
    code = random.randint(100000, 999999)
    return code



def generate_valid_password(length=10):
    if length < 2:
        raise ValueError("Password length must be at least 2")

    # обязательные символы
    letters = string.ascii_letters
    digits = string.digits

    # хотя бы одна буква и одна цифра
    password_chars = [
        secrets.choice(letters),
        secrets.choice(digits),
    ]

    # остальные символы из общего алфавита
    alphabet = letters + digits
    password_chars.extend(secrets.choice(alphabet) for _ in range(length - 2))

    # перемешиваем, чтобы цифра не была всегда второй
    random.shuffle(password_chars)

    return ''.join(password_chars)

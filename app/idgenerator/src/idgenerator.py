import random
import string
import secrets
import uuid
# if the below line does not have the dot, it will throw error
# Traceback (most recent call last):
#   File "/Users/yijun/qrojects/python_package_example/run.py", line 1, in <module>
#     from idgenerator import generate_credit_card_number, generate_guid, generate_object_id, generate_password
#   File "/Users/yijun/qrojects/python_package_example/venv/lib/python3.10/site-packages/idgenerator/__init__.py", line 1, in <module>
#     from .src.idgenerator import (
#   File "/Users/yijun/qrojects/python_package_example/venv/lib/python3.10/site-packages/idgenerator/src/idgenerator.py", line 5, in <module>
#     from utils import luhn_checksum
# ModuleNotFoundError: No module named 'utils'
from .utils import luhn_checksum
import bson


def generate_password(length: int = 6) -> str:
    """Generate a random password of a given length."""
    assert length >= 6, f"Password length must be at least 6 characters long, got {length}"
    while True:
        pwd = ""
        for i in range(length):
            pwd += "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation))
        if (any(c.islower() for c in pwd)
                and any(c.isupper() for c in pwd)
                and any(c in string.punctuation for c in pwd)
                and any(c in string.digits for c in pwd)
            ):
            break
    return pwd


def generate_guid() -> str:
    """Generate a random GUID."""
    return str(uuid.uuid4()).upper()


def generate_credit_card_number(length: int = 8) -> str:
    """Generate a random credit card number."""
    number = "".join(random.choices(string.digits, k=length))
    while not luhn_checksum(number):
        number = "".join(random.choices(string.digits, k=length))
    return number


def generate_object_id() -> str:
    """Generate a random object ID."""
    return str(bson.ObjectId())


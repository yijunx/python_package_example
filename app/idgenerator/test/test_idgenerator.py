import unittest
import string
from ..src.idgenerator import generate_credit_card_number, generate_guid, generate_object_id, generate_password
from ..src.utils import luhn_checksum


class GeneratorTest(unittest.TestCase):
    def test_generate_password(self) -> None:
        pwd = generate_password()
        self.assertEqual(len(pwd), 6)
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))
        self.assertTrue(any(c in string.digits for c in pwd))
        self.assertRaises(AssertionError, generate_password, 5)

    def test_generate_guid(self) -> None:
        guid = generate_guid()
        self.assertEqual(len(guid), 36)
        self.assertEqual(guid.count("-"), 4)
    
    def test_generate_credit_card_number(self) -> None:
        number = generate_credit_card_number(16)
        self.assertEqual(len(number), 16)
        self.assertTrue(luhn_checksum(number))
    
    def test_generate_object_id(self) -> None:
        oid = generate_object_id()
        self.assertEqual(len(oid), 24)
        self.assertEqual(oid.count("-"), 0)
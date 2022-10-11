import unittest
from app.models import User


class UserModelCase(unittest.TestCase):
    def test_password_hashing(self):
        u = User(username='usertest')
        u.set_password('passwordTest')
        self.assertFalse(u.check_password('fakePassword'))
        self.assertTrue(u.check_password('passwordTest'))
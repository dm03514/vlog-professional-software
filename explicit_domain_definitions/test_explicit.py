import unittest
from explicit import create_user, enroll_user, User


class ImplicitTestCase(unittest.TestCase):
    def test_user_id(self):
        self.assertEqual(
            'firstlast',
            create_user(
                first_name = 'first',
                last_name = 'last'
            ).id
        )

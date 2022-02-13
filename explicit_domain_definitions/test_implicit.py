import unittest
from unittest.mock import patch

from implicit import enroll_user


class ImplicitTestCase(unittest.TestCase):

    @patch('implicit.insert_user_into_db')
    def test_enroll_user(self, mock_insert):
        enroll_user(
            first_name='first',
            last_name='last'
        )
        mock_insert.assert_called_once_with(
            'firstlast',
            'first',
            'last'
        )
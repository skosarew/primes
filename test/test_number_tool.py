import unittest

from number_tool import get_prime_multipliers


class TestNumberTool(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertEquals(get_prime_multipliers(63), [3, 3, 7])
        self.assertEquals(get_prime_multipliers(1023), [3, 11, 31])
        self.assertNotEquals(get_prime_multipliers(1023), [3.0, 11.0])

import unittest
import check


class MyTestCase(unittest.TestCase):
    def test_is_prime_candidate(self):
        self.assertFalse(check.is_prime_candidate(0))
        self.assertTrue(check.is_prime_candidate(1))
        self.assertFalse(check.is_prime_candidate(2))
        self.assertTrue(check.is_prime_candidate(3))
        self.assertFalse(check.is_prime_candidate(4))
        self.assertFalse(check.is_prime_candidate(5))
        self.assertFalse(check.is_prime_candidate(6))
        self.assertTrue(check.is_prime_candidate(7))
        self.assertFalse(check.is_prime_candidate(8))
        self.assertTrue(check.is_prime_candidate(9))
        self.assertFalse(check.is_prime_candidate(10))

    def test_calculate_mod_10_checksum(self):
        self.assertEqual(0, check.calculate_mod_10_checksum(0))
        self.assertEqual(8, check.calculate_mod_10_checksum(1))
        self.assertEqual(6, check.calculate_mod_10_checksum(2))
        self.assertEqual(4, check.calculate_mod_10_checksum(3))
        self.assertEqual(2, check.calculate_mod_10_checksum(4))
        self.assertEqual(9, check.calculate_mod_10_checksum(5))
        self.assertEqual(7, check.calculate_mod_10_checksum(6))
        self.assertEqual(5, check.calculate_mod_10_checksum(7))
        self.assertEqual(3, check.calculate_mod_10_checksum(8))
        self.assertEqual(1, check.calculate_mod_10_checksum(9))
        self.assertEqual(8, check.calculate_mod_10_checksum(10))


if __name__ == '__main__':
    unittest.main()

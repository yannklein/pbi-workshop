import unittest
from speed_controller import multiplicator, basic_tax, total_tax


class TestSpeedController(unittest.TestCase):
    def test_multiplicator(self):
        self.assertEqual(multiplicator(50, 51), 1)
        self.assertEqual(multiplicator(50, 60), 2)
        self.assertEqual(multiplicator(50, 75), 4)
        self.assertEqual(multiplicator(50, 101), 32)

    def test_basic_tax(self):
        self.assertEqual(basic_tax(50, 51), 12.5)
        self.assertEqual(basic_tax(50, 60), 50)
        self.assertEqual(basic_tax(50, 65), 75)

    def test_total_tax(self):
        self.assertEqual(total_tax(50, 51), 12.5)
        self.assertEqual(total_tax(50, 62), 120)
        self.assertEqual(total_tax(50, 56), 30)
        self.assertEqual(total_tax(50, 70), 400)

    def test_no_infraction(self):
        self.assertEqual(total_tax(50, 49), 'no infraction committed')
        self.assertEqual(total_tax(50, 50), 'no infraction committed')


if __name__ == '__main__':
    unittest.main()

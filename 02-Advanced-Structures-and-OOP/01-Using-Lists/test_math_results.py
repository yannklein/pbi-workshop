import unittest
from maths_results import get_students_starting_with, get_score_position, \
    get_score_unknown_position, average_math_result, not_participating, student_who_succeeded


class TestMathResults(unittest.TestCase):
    def test_get_student_first_letter(self):
        students = ["Tanguy", "Amine", "Lucile", "Ben", "Eric", "Michael", "Tom"]
        self.assertEqual(get_students_starting_with(students, 'T'), ["Tanguy", "Tom"])
        self.assertEqual(get_students_starting_with(students, 'd'), [])

    def test_get_score(self):
        results = [["Tanguy", 5], ["Lucile", 8], ["Amine", 7], ["Eric", 10], ["Michael", 0]]
        self.assertEqual(get_score_position(results, 0), 5)
        self.assertEqual(get_score_unknown_position(results, 'Tanguy'), 5)

    def test_average_math_result(self):
        results = [["Tanguy", 5], ["Lucile", 8], ["Amine", 7], ["Eric", 10], ["Michael", 0]]
        self.assertEqual(average_math_result(results), 6.0)

    def test_student_who_succeeded(self):
        results = [["Tanguy", 5], ["Lucile", 8], ["Amine", 7], ["Eric", 10], ["Michael", 0]]
        self.assertEqual(sorted(student_who_succeeded(results)), sorted(["Tanguy", "Lucile", "Amine", "Eric"]))

    def test_not_participating(self):
        students = ["Tanguy", "Amine", "Lucile", "Ben", "Eric", "Michael", "Tom"]
        results = [["Tanguy", 5], ["Lucile", 8], ["Amine", 7], ["Eric", 10], ["Michael", 0]]
        self.assertEqual(not_participating(students, results), ["Ben", "Tom"])


if __name__ == '__main__':
    unittest.main()

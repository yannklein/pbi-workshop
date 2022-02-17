import unittest
from extractor import extract, treatment


class TestExtractor(unittest.TestCase):
    def test_extract(self):
        stu_ans = extract('leWagon42')
        corr_ans = 'consonant-low vowel-low consonant-up vowel-low consonant-low vowel-low consonant-low number number'
        self.assertEqual(stu_ans.strip(), corr_ans)

    def test_extract_char_y(self):
        a = 'y'
        stu_ans = extract(a)
        corr_ans = 'vowel-low'
        self.assertEqual(stu_ans.strip(), corr_ans)

    def test_extract_upper(self):
        stu_ans = extract('ABBA')
        corr_ans = 'vowel-up consonant-up consonant-up vowel-up'
        self.assertEqual(stu_ans.strip(), corr_ans)

    def test_extract_number(self):
        stu_ans = extract('42')
        corr_ans = 'number number'
        self.assertEqual(stu_ans.strip(), corr_ans)

    def test_extract_trailing_space(self):
        stu_ans = extract('abba')
        corr_ans = 'vowel-low consonant-low consonant-low vowel-low'
        self.assertEqual(stu_ans, corr_ans)

    def test_treatment(self):
        stu_ans = treatment('vowel-low consonant-low consonant-low vowel-low')
        corr_ans = 'vowel-low*1 consonant-low*2 vowel-low*1'
        self.assertEqual(stu_ans.strip(), corr_ans)

    def test_treatment_trailing_space(self):
        stu_ans = treatment('vowel-low consonant-low consonant-low vowel-low')
        corr_ans = 'vowel-low*1 consonant-low*2 vowel-low*1'
        self.assertEqual(stu_ans, corr_ans)


if __name__ == '__main__':
    unittest.main()

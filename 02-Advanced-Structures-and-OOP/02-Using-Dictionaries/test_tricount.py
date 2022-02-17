import unittest
from tricount import add_user, add_amount, get_spent_amount, \
    total_amount, get_due_amount, debts_dictionary, delete


class TestTricountWithDictionary(unittest.TestCase):

    def test_add_user(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        self.assertEqual(len(tri_count_dic), 4)
        add_user(tri_count_dic, 'Amine')
        self.assertEqual(len(tri_count_dic), 5)

    def test_add_amount(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        add_amount(tri_count_dic, 'Eric', 20.0)
        self.assertEqual(tri_count_dic["Eric"], 20.0)

    def test_amount_spent(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        self.assertEqual(get_spent_amount(tri_count_dic, 'Tanguy'), 40.0)

    def test_total_amount(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        self.assertEqual(total_amount(tri_count_dic), 60.0)

    def test_amount_due(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        self.assertEqual(get_due_amount(tri_count_dic, 'Lucile'), 15.0)
        self.assertEqual(get_due_amount(tri_count_dic, 'Tanguy'), -25.0)

    def test_debts_dictionary(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        debts = debts_dictionary(tri_count_dic, 'Lucile')
        self.assertEqual(debts['Tanguy'], 10.0)
        self.assertEqual(debts['Eric'], 0.0)
        self.assertEqual(debts['Michael'], 5.0)

    def test_delete(self):
        tri_count_dic = {"Eric": 0.0, "Tanguy": 40.0, "Lucile": 0.0, 'Michael': 20.0}
        delete(tri_count_dic, 'Lucile')
        self.assertEqual(len(tri_count_dic), 3)


if __name__ == '__main__':
    unittest.main()

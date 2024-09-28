import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_normal_cases(self):
        """Обычные случаи"""
        self.assertEqual(merge_sort([10, 3, 6, 2, 8, 5]), [2, 3, 5, 6, 8, 10],
                         "Expected [2, 3, 5, 6, 8, 10]")
        self.assertEqual(merge_sort([11, 9, 7, 5, 3, 1]), [1, 3, 5, 7, 9, 11],
                         "Expected [1, 3, 5, 7, 9, 11]")

    def test_edge_cases(self):
        """Краевые случаи"""
        self.assertEqual(merge_sort([]), [], "Expected []")
        self.assertEqual(merge_sort([99]), [99], "Expected [99]")

    def test_duplicates(self):
        """Повторяющиеся элементы"""
        self.assertEqual(merge_sort([12, 15, 12, 9, 8, 15]), [8, 9, 12, 12, 15, 15],
                         "Expected [8, 9, 12, 12, 15, 15]")

    def test_floats(self):
        """Вещественные числа"""
        self.assertEqual(merge_sort([7.1, 3.3, 8.8, 2.2, 6.6]), [2.2, 3.3, 6.6, 7.1, 8.8],
                         "Expected [2.2, 3.3, 6.6, 7.1, 8.8]")

    def test_negative_numbers(self):
        """Отрицательные числа"""
        self.assertEqual(merge_sort([4, -3, -7, 0, 2]), [-7, -3, 0, 2, 4],
                         "Expected [-7, -3, 0, 2, 4]")

    def test_mixed_numbers(self):
        """Смешанные отрицательные и положительные числа"""
        self.assertEqual(merge_sort([-10, 7, -3, 1, -1]), [-10, -3, -1, 1, 7],
                         "Expected [-10, -3, -1, 1, 7]")

    def test_invalid_input(self):
        """Ошибочные случаи"""
        with self.assertRaises(TypeError):
            merge_sort("invalid input")

        with self.assertRaises(ValueError):
            merge_sort([4, 5, 'seven', 8])


if __name__ == '__main__':
    unittest.main()

import unittest


class BubbleSort:
    def sort(self, seq: list) -> list:
        changed = True

        while changed:
            changed = False
            for index in range(len(seq) - 1):
                if seq[index] > seq[index + 1]:
                    seq[index], seq[index + 1] = seq[index + 1], seq[index]
                    changed = True

        return seq


class BubbleSortTest(unittest.TestCase):
    def setUp(self) -> None:
        print(f'Run {self._testMethodName}.')

    def test_str_int_comparison(self) -> None:
        with self.assertRaises(TypeError):
            bs.sort(test_cases['mix_str_int_list'])

    def test_empty_list(self) -> None:
        bubble_sort_result = bs.sort(test_cases['empty_list'])
        self.assertEqual(
            test_cases['empty_list'],
            bubble_sort_result
        )

    def test_positive_integer(self) -> None:
        bubble_sort_result = bs.sort(test_cases['positive_integer_list'])
        self.assertEqual(
            test_cases['sorted_positive_integer_list'],
            bubble_sort_result
        )

    def test_negative_integer(self) -> None:
        bubble_sort_result = bs.sort(test_cases['negative_integer_list'])
        self.assertEqual(
            test_cases['sorted_negative_integer_list'],
            bubble_sort_result
        )

    def test_positive_float(self) -> None:
        bubble_sort_result = bs.sort(test_cases['positive_float_list'])
        self.assertEqual(
            test_cases['sorted_positive_float_list'],
            bubble_sort_result
        )

    def test_negative_float(self) -> None:
        bubble_sort_result = bs.sort(test_cases['negative_float_list'])
        self.assertEqual(
            test_cases['sorted_negative_float_list'],
            bubble_sort_result
        )

    def test_str_list(self) -> None:
        bubble_sort_result = bs.sort(test_cases['str_list'])
        self.assertEqual(
            test_cases['sorted_str_list'],
            bubble_sort_result
        )


bs = BubbleSort()
test_cases = {
    'mix_str_int_list': ['1', 1],
    'empty_list': [],
    'positive_integer_list': [40, 4, 3, 2, 13],
    'sorted_positive_integer_list': [2, 3, 4, 13, 40],
    'negative_integer_list': [-1, -2, -3],
    'sorted_negative_integer_list': [-3, -2, -1],
    'positive_float_list': [5.5, 4.4, 3.3, 0.5, 69.9],
    'sorted_positive_float_list': [0.5, 3.3, 4.4, 5.5, 69.9],
    'negative_float_list': [-5.5, -10.0, -3.3],
    'sorted_negative_float_list': [-10.0, -5.5, -3.3],
    'str_list': ['111', 'apple', 'orange', 'ржавый', 'возвращение на родину'],
    'sorted_str_list': ['111', 'apple', 'orange', 'возвращение на родину', 'ржавый']
}


if __name__ == '__main__':
    unittest.main()

"""
Doctests для merge_sort, разделенные по группам.

Обычные случаи:

>>> from merge_sort import merge_sort
>>> merge_sort([10, 3, 6, 2, 8, 5])
[2, 3, 5, 6, 8, 10]
>>> merge_sort([11, 9, 7, 5, 3, 1])
[1, 3, 5, 7, 9, 11]

Краевые случаи:

>>> merge_sort([])
[]
>>> merge_sort([99])
[99]

Повторяющиеся элементы:

>>> merge_sort([12, 15, 12, 9, 8, 15])
[8, 9, 12, 12, 15, 15]

Вещественные числа:

>>> merge_sort([7.1, 3.3, 8.8, 2.2, 6.6])
[2.2, 3.3, 6.6, 7.1, 8.8]

Отрицательные числа:

>>> merge_sort([4, -3, -7, 0, 2])
[-7, -3, 0, 2, 4]

Смешанные отрицательные и положительные числа:

>>> merge_sort([-10, 7, -3, 1, -1])
[-10, -3, -1, 1, 7]

Ошибочные случаи:

>>> merge_sort("invalid input")  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
TypeError: Input must be a list

>>> merge_sort([4, 5, 'seven', 8])  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
ValueError: All list elements must be numeric
"""

import doctest

if __name__ == "__main__":
    doctest.testmod()

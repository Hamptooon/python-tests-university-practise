
from merge_sort import merge_sort

def test_1():
    # Обычные случаи
    assert merge_sort([10, 3, 6, 2, 8, 5]) == [2, 3, 5, 6, 8, 10], \
        f"Expected [2, 3, 5, 6, 8, 10], but got {merge_sort([10, 3, 6, 2, 8, 5])}"
    assert merge_sort([11, 9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9, 11], \
        f"Expected [1, 3, 5, 7, 9, 11], but got {merge_sort([11, 9, 7, 5, 3, 1])}"

def test_2():
    # Краевые случаи
    assert merge_sort([]) == [], f"Expected [], but got {merge_sort([])}"
    assert merge_sort([99]) == [99], f"Expected [99], but got {merge_sort([99])}"

def test_3():
    # Повторяющиеся элементы
    assert merge_sort([12, 15, 12, 9, 8, 15]) == [8, 9, 12, 12, 15, 15], \
        f"Expected [8, 9, 12, 12, 15, 15], but got {merge_sort([12, 15, 12, 9, 8, 15])}"

def test_4():
    # Вещественные числа
    assert merge_sort([7.1, 3.3, 8.8, 2.2, 6.6]) == [2.2, 3.3, 6.6, 7.1, 8.8], \
        f"Expected [2.2, 3.3, 6.6, 7.1, 8.8], but got {merge_sort([7.1, 3.3, 8.8, 2.2, 6.6])}"

def test_5():
    # Отрицательные числа
    assert merge_sort([4, -3, -7, 0, 2]) == [-7, -3, 0, 2, 4], \
        f"Expected [-7, -3, 0, 2, 4], but got {merge_sort([4, -3, -7, 0, 2])}"

def test_6():
    # Смешанные отрицательные и положительные числа
    assert merge_sort([-10, 7, -3, 1, -1]) == [-10, -3, -1, 1, 7], \
        f"Expected [-10, -3, -1, 1, 7], but got {merge_sort([-10, 7, -3, 1, -1])}"

def test_7():
    # Ошибочные случаи
    try:
        merge_sort("invalid input")
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError when sorting a non-list")

    try:
        merge_sort([4, 5, 'seven', 8])
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when list contains non-numeric elements")

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()

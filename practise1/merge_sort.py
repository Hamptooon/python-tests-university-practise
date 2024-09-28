def merge_sort(nums):
    if not isinstance(nums, list):  # --аргумент является списком--
        raise TypeError("Аргумент должен быть списком")

    elif not all(isinstance(x, (int, float)) for x in nums):  # --проверка, что все элементы списка числа--
        raise ValueError("Все элементы списка должны быть числами")

    elif len(nums) <= 1:
        return nums

    # Разделение списка на две части
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Слияние отсортированных частей
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)

    while left_list_index < left_list_length and right_list_index < right_list_length:
        # Сравниваем элементы из обеих половин и добавляем в отсортированный список меньший
        if left_list[left_list_index] <= right_list[right_list_index]:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
        else:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

    # Добавляем оставшиеся элементы из левой части, если они есть
    while left_list_index < left_list_length:
        sorted_list.append(left_list[left_list_index])
        left_list_index += 1

    # Добавляем оставшиеся элементы из правой части, если они есть
    while right_list_index < right_list_length:
        sorted_list.append(right_list[right_list_index])
        right_list_index += 1

    return sorted_list

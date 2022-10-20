def binary_search(element, some_list):
    a = 0
    b = len(some_list) - 1
    while a <= b:
        index_avg = (a + b) // 2
        if some_list[index_avg] == element:
            return index_avg
        elif some_list[index_avg] > element:
            b = index_avg - 1
        else:
            a = index_avg + 1
    return None


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

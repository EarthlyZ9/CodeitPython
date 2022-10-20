def find_same_number(some_list, start=1, end=None):
    if end == None:
        end = len(some_list) - 1
    if start == end:
        return start

    mid = (start + end) // 2
    left_count = 0
    for i in some_list:
        if i >= start and i <= mid:
            left_count += 1
    if left_count > mid - start + 1:
        return find_same_number(some_list, start, mid)
    return find_same_number(some_list, mid + 1, end)

    # if end == None:
    #     end = len(some_list) - 1
    # index_number = 0
    #     while index_number < len(some_list) - 1:
    #         for i in range(index_number + 1,):
    #             if some_list[index_number + 1] == some_list[i]:
    #                 return some_list[i]
    #         index_number += 1


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))

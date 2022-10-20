# merge함수: 정렬된 두 리스트를 합쳐주는 함
def merge(list1, list2):
    i = 0
    j = 0
    list3 = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1
        # 최종 리스트에서 중복된 원소를 하나만 포함하려면:
        # if list1[i] < list2[j]:
        #     list3.append(list1[i])
        #     i += 1
        # elif list1[i] > list2[j]:
        #     list3.append(list2[j])
        #     j += 1
        # else:
        #     list3.append(list1[i])
        #     i += 1
        #     j += 1

    if i != len(list1):
        list3 = list3 + list1[i:]
    elif j != len(list2):
        list3 = list3 + list2[j:]

    return list3


# 합병 정렬
def merge_sort(my_list):
    mid_index = (len(my_list) - 1) // 2
    if len(my_list) < 2:
        return my_list

    return merge(
        merge_sort(my_list[: mid_index + 1]), merge_sort(my_list[mid_index + 1 :])
    )


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))

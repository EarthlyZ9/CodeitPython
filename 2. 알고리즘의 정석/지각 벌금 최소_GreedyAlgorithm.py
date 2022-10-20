def min_fee(pages_to_print):
    pages_list = sorted(pages_to_print)
    i = len(pages_list)
    sum = 0
    a = 0
    while i > 0:
        for b in pages_list:
            a = b * i
            i -= 1
            sum = sum + a
        return sum

    # pages_list = sorted(pages_to_print)
    # total_fee = 0
    # for i in range(len(pages_list)):
    #     total_fee += pages_list[i] * (len(pages_list) - i)
    # return total_fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))

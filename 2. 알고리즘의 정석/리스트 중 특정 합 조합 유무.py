def sum_in_list(search_sum, sorted_list):
    for i in sorted_list:
        if search_sum - i in sorted_list:
            return True
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))

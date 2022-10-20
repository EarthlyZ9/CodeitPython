def fib_tab(n):

    fib_table = [0, 1, 1]
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 2] + fib_table[i - 1])
    return fib_table[n]


# 공간최적화
# def fib_optimized(n):
#     previous = 0
#     temp = 0
#     current = 1
#     for i in range(2, n + 1):
#         temp = current
#         current = current + previous
#         previous = temp
#     return current


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

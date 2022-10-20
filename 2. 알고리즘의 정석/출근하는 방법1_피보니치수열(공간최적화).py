# def factorial(n):
#     if n <= 1:
#         return 1
#     return factorial(n - 1) * n
#
# def staircase(n):
#     if n == 0:
#         return 1
#     else:
#         number_of_1 = n
#         number_of_2 = 0
#         sum = 0
#         single_case = 0
#         for i in range((n // 2) + 1):
#             single_case = int(factorial((n - 2 * i) + i ) / (factorial(n - 2 * i) * factorial(i)))
#             sum = sum + single_case
#         return sum


def staircase(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))

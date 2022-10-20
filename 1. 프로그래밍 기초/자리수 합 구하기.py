def sum_digit(num):
    each_digit = list(str(num))
    # print(each_digit)
    for i in range(len(each_digit)):
        each_digit[i] = int(each_digit[i])
    # print(each_digit)
    a = 0
    for j in range(len(each_digit)):
        a = a + each_digit[j]
    return a


b = 0
for c in range(1, 1001):
    b = b + sum_digit(c)
print(b)

# list 말고 str 이용해서 풀기
# # 자리수 합 리턴
# def sum_digit(num):
#     each_digit = str(num)
#     a = 0
#     #print(each_digit)
#     for i in each_digit:
#         a = a + int(i)
#     return a
#
# # sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# b = 0
# for c in range(1, 1001):
#     b = b + sum_digit(c)
# print(b)

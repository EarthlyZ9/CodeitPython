# 1000보다 작은 자연수 중 2 또는 3의 배수의 합 출력하기
i = 1
a = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        a = a + i
    i = i + 1
print(a)

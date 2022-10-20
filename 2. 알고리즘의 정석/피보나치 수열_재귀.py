# 1 이상 자연수 n, n번째 피보니차 수열 리
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


for i in range(1, 11):
    print(fib(i))

print(fib(10))

# 각 단계마다 풀어야하는 문제가 두배씩 증가하므로 시간복잡도는 O(2^n)

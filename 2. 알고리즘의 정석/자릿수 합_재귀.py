def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(n // 10) + (n % 10)


print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# d를 자릿수 개수라고 하면, sum_digits는 호출할 때하마 자릿수가 하나씩 줄어들기 때문에 시간 복잡도는 O(d)

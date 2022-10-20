numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for i in range(round(len(numbers) / 2)):
    a = numbers[i]
    numbers[i] = numbers[6 - i]
    numbers[6 - i] = a

print("뒤집어진 리스트: " + str(numbers))

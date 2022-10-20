from random import randint

numbers = []
while len(numbers) < 3:
    new_number = randint(0, 9)
    while new_number in numbers:
        new_number = randint(0, 9)
    numbers.append(new_number)
print(numbers)

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print()
num_1 = 0
num_2 = 0
num_3 = 0
input_nums = [num_1, num_2, num_3]
count = 0
while numbers != input_nums:
    while count < 3:
        print("세 수를 하나씩 차례대로 입력하세요.")
        num_1 = int(input("1번째 수를 입력하세요: "))
    while num_1 > 9 or num_1 < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        num_1 = int(input("1번째 수를 입력하세요: "))
    num_2 = int(input("2번째 수를 입력하세요: "))
    while num_2 == num_1:
        print("중복되는 수 입니다. 다시 입력해주세요.")
        num_2 = int(input("2번째 수를 입력하세요: "))
    while num_2 > 9 or num_2 < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        num_2 = int(input("2번째 수를 입력하세요: "))
    num_3 = int(input("3번째 수를 입력하세요: "))
    while num_2 == num_3:
        print("중복되는 수 입니다. 다시 입력해주세요.")
        num_3 = int(input("3번째 수를 입력하세요: "))
    while num_3 > 9 or num_3 < 0:
        print("범위를 벗어나는 수입니다. 다시 입력해주세요.")
        num_3 = int(input("3번째 수를 입력하세요: "))
    input_nums = [num_1, num_2, num_3]
    print(input_nums)
    count = count + 1

    S = 0
    B = 0
    if num_1 in numbers:
        if numbers.index(num_1) == 0:
            S = S + 1
        else:
            B = B + 1
    if num_2 in numbers:
        if numbers.index(num_2) == 1:
            S = S + 1
        else:
            B = B + 1
    if num_3 in numbers:
        if numbers.index(num_3) == 2:
            S = S + 1
        else:
            B = B + 1
    print("{}S {}B".format(S, B))
print("축하합니다. {}번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(count))
